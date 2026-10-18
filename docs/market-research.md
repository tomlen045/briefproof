# BriefProof: opportunity and market scan

Research snapshot: 18 October 2026. This is a directional desk scan, not a full market-size study or proof of willingness to pay.

## Opportunity selected

**Evidence-backed acceptance for creator deliverables:** translate a real campaign/production brief into checkable requirements, spot ambiguity before review, and compare the final video and its supporting copy/subtitles against those requirements with timestamped or quoted evidence.

The AI-specific unlock is multimodal reasoning over a brief plus video frames, speech text, and publish metadata. Earlier rule-based tools could find strings or check duration; a strong model can interpret varied briefs and judge whether a visual instruction is actually present. The product must still ground every verdict in an artifact and mark uncertain cases for a person.

## Signals

- A 2025 Visa creator survey covered 1,067 creators across five countries and identifies payment delays as a creator-business pain point. This supports the wider need for reliable creator operations, but is not direct proof of demand for a video acceptance tool. [Visa, 2025 Creator Report](https://corporate.visa.com/en/solutions/commercial-solutions/knowledge-hub/2025-visa-creators-report.html)
- In a 2026 creator discussion about repurposing, a highly specific response said the time sink was reviewing and selecting moments after automatic clipping. That validates the general burden of review, but our separate search found semantic footage search is already crowded; we dropped that idea. [Reddit discussion](https://www.reddit.com/r/contentcreation/comments/1r3sbv8/im_19_and_building_a_tool_for_content_creators/)
- Commercial products explicitly sell checking videos against campaign briefs, using speech, image, caption, and timestamp evidence. That is strong evidence the buyer problem is real, and equally strong evidence that the category itself is not empty. Examples: [OnBriefing](https://onbriefing.com/), [Vibe Analytics Brief Analyzer](https://vibeanalytics.com/products/brief-analyzer/), and [Content Approval](https://content-approval.ai/).
- The open-source GitHub scan surfaced a narrow multimodal video audit prototype and several AI-video storyboard/quality utilities, but not an established, broadly adopted local-first brief-to-evidence acceptance product with a portable Agent Skill. Examples: [multimodal-audit-engine](https://github.com/shiv669/multimodal-audit-engine), [Video Quality Auditor](https://github.com/CineInfini/Video_Quality_Auditor), and [ai-video-production-verifier](https://github.com/martinsaguinaga315-dot/ai-video-production-verifier).
- A creator-economy survey indicates a large population, but it should not be read as the addressable market for this specific tool. [Visa 2025 report](https://corporate.visa.com/en/solutions/commercial-solutions/knowledge-hub/2025-visa-creators-report.html)

## Competition and differentiation

| Alternative | What it does | What BriefProof tries to add |
|---|---|---|
| Hosted creator campaign reviewers | Run checks at agency/brand scale on uploaded or published deliverables | Local-first, inspectable, no hosted account, adaptable to a user's existing brief, with a portable agent workflow |
| Video editing suites / footage search | Find moments and accelerate editing | Not our focus; this segment is already served by Adobe, Apple, and new open-source projects |
| Basic moderation / video-quality code | Detect safety categories or technical quality signals | Requirement-by-requirement comparison to a specific brief, including brief ambiguity and evidence references |
| Generic agent prompt | Review a brief and video informally | Explicit verdict policy, source excerpts, timestamps/quotes, consistent `review` state, and reusable report format |

## Fit with existing work

The author's earlier creator-tooling work covers Chinese creator production, publishing preparation, and analytics, including `title-referee` for headline quality and clickbait risk. Neither repository has a brief compiler or a multimodal, evidence-citing acceptance loop across video, transcript, and publish copy. BriefProof therefore extends that creator-tooling experience without duplicating those products.

## Why not the other candidates

1. **Natural-language footage search:** strong pain signal, but several fresh open-source projects and major editors already cover it. Too crowded for the requested greenfield positioning.
2. **Generic AI video generation/repurposing:** high visible demand, but crowded and primarily competes on model access and rendering volume.
3. **Title/thumbnail scoring:** overlaps directly with `title-referee` and creator analytics already in the user's work.

## Adoption hypothesis and falsification

The plausible route toward a 10,000-user open-source tool is a narrow reusable workflow that benefits creators, small agencies, and coding agents: put the skill on GitHub, give it a useful local UI, support BYO compatible models, and make reports easy to export. A 10k outcome is an ambition, not a forecast. Existing paid products show buyer value but also create a high bar for accuracy and workflow integration.

The product hypothesis should be rejected or repositioned if independent creators and small agencies do not regularly receive brief-driven deliverables, if current campaign tools already fit their needs, or if the model's evidence citations are too unreliable to reduce review time. The first validation signal should be repeat weekly use on real briefs, not GitHub stars alone.

## Search limitations

The local Agent Reach doctor found no authenticated GitHub CLI session and no configured Exa/social backends. Public web search was used to inspect GitHub repositories, product pages, and community discussions. Consequently, “no established match found” is a scoped finding from a public search scan, not a claim that no similar repository or private product exists. No authenticated account history could be checked for unpushed or private repositories; the local inventory review covered the visible creator projects on this machine.
