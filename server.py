#!/usr/bin/env python3
"""BriefProof local web app and OpenAI-compatible model proxy."""
from __future__ import annotations

import json
import mimetypes
import os
import re
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATIC = ROOT / "static"


def model_call(payload: dict) -> dict:
    settings = payload.get("settings") or {}
    base = (settings.get("baseUrl") or "https://api.openai.com/v1").rstrip("/")
    key = settings.get("apiKey", "")
    model = settings.get("model", "")
    if not model:
        raise ValueError("先填写模型名称。")
    if not base.startswith(("https://", "http://127.0.0.1", "http://localhost")):
        raise ValueError("模型地址必须使用 HTTPS；本机服务可用 localhost。")

    req = urllib.request.Request(
        base + "/chat/completions",
        data=json.dumps({"model": model, "temperature": 0.1, "messages": payload["messages"]}).encode(),
        headers={"Content-Type": "application/json", **({"Authorization": f"Bearer {key}"} if key else {})},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            body = json.loads(response.read())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:1200]
        raise RuntimeError(f"模型接口返回 HTTP {exc.code}: {detail}") from exc
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"无法连接模型接口：{exc}") from exc
    try:
        answer = body["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError("模型响应中没有 choices[0].message.content。") from exc
    if isinstance(answer, list):
        answer = "\n".join(part.get("text", "") for part in answer if isinstance(part, dict))
    answer = re.sub(r"^\s*```(?:json)?\s*|\s*```\s*$", "", str(answer), flags=re.I)
    try:
        return json.loads(answer)
    except json.JSONDecodeError as exc:
        raise RuntimeError("模型没有返回有效 JSON。请换支持 JSON 指令的模型再试。") from exc


class Handler(BaseHTTPRequestHandler):
    def _send(self, status: int, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._send(200, b'{"ok":true}', "application/json; charset=utf-8")
            return
        path = (STATIC / ("index.html" if self.path == "/" else self.path.lstrip("/"))).resolve()
        if STATIC.resolve() not in path.parents and path != STATIC.resolve():
            self._send(403, b"Forbidden", "text/plain; charset=utf-8")
            return
        if not path.is_file():
            self._send(404, b"Not found", "text/plain; charset=utf-8")
            return
        self._send(200, path.read_bytes(), mimetypes.guess_type(path.name)[0] or "application/octet-stream")

    def do_POST(self) -> None:
        if self.path != "/api/analyze":
            self._send(404, b'{"error":"Not found"}', "application/json; charset=utf-8")
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length > 28_000_000:
                raise ValueError("本次素材过大，请减少截图或降低采样频率。")
            data = json.loads(self.rfile.read(length))
            result = model_call(data)
            body = json.dumps({"result": result}, ensure_ascii=False).encode()
            self._send(200, body, "application/json; charset=utf-8")
        except Exception as exc:  # surface actionable errors to the local UI
            body = json.dumps({"error": str(exc)}, ensure_ascii=False).encode()
            self._send(400, body, "application/json; charset=utf-8")

    def log_message(self, fmt: str, *args) -> None:
        # Avoid logging request bodies or credentials.
        print(f"[BriefProof] {self.address_string()} {fmt % args}")


if __name__ == "__main__":
    port = int(os.environ.get("BRIEFPROOF_PORT", "8765"))
    print(f"BriefProof listening at http://127.0.0.1:{port}")
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
