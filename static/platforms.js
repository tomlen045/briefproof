// BriefProof platform presets. Each preset injects extra hard requirements
// into the analysis. Rules are editable in the UI; treat them as a baseline
// and defer to the platform's latest community guidelines.
window.PLAT = {
  douyin: {
    label: '抖音',
    note: '预设是通用基线，以抖音最新社区公约与星图规范为准；可在下方文本框直接修改。',
    rules: [
      '【画幅与清晰度】竖屏 9:16，建议分辨率 1080×1920，画面清晰不糊底。',
      '【安全区】字幕、品牌标识、二维码等关键信息避开右侧互动按钮栏（约右侧 15% 宽）、底部约 20% 高的文案与进度区、顶部状态栏遮挡区。',
      '【时长】成片时长与内容结构匹配；平台常规短视频以 60 秒内完播率优先（以 brief 约定为准）。',
      '【字幕】全程硬字幕，字号清晰；口播与字幕一致。',
      '【商业内容】品牌合作内容须经星图等官方渠道报备，发布时勾选商业合作/广告声明；不得未报备发布软广。',
      '【文案与话题】发布文案含 #话题标签，按 brief 要求携带指定话题；文案不堆砌无关热词。',
      '【违禁与极限词】口播、字幕、文案不出现《广告法》极限词（最、第一、绝对、国家级等）与医疗功效断言；食品、化妆品不做治疗/治愈类宣称。',
      '【站内合规】不出现站外引流信息（微信号、二维码、外链）；不诱导站外抽奖或跳转。',
    ].join('\n'),
  },
};
