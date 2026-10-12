# `MiniMax-H3`

The identifier is case-sensitive.

## Script

```bash
python3 {baseDir}/scripts/create_model_generation.py "USER_PROMPT" \
  --model MiniMax-H3 [options]
```

## 参数拼装

Omitted `--resolution` becomes `768P`. The document requires a resolution and does not name one, so this is the tier nearest 720p. Text-only requests use `--aspect-ratio 16:9` because `adaptive` is forbidden. With an image or video, the omitted ratio becomes `adaptive`, which the document applies automatically. `--duration` is still required. Explicit flags win.

| Intent | Flag | Rule |
|---|---|---|
| Output seconds | `--duration N` | Required upstream range `4`–`15` |
| Aspect ratio | `--aspect-ratio VALUE` | `adaptive`, `9:16`, `16:9`, `4:3`, `3:4`, `1:1`, `21:9`; pure text requires a non-adaptive value |
| Resolution | `--resolution VALUE` | Exact `768P` or `2K` |
| Primary/reference images | image flags | Upload first |
| Reference videos | repeat `--reference-video-id ID` | Total ≤15 seconds |
| Reference audio | `--audio-upload-id ID` | Requires compatible visual input |

```bash
python3 {baseDir}/scripts/create_model_generation.py "电影感城市延时摄影" \
  --model MiniMax-H3 --duration 5 --resolution 2K --aspect-ratio 16:9
```

## 不可用能力

The upstream supports explicit first/last-frame roles, but the Gateway cannot transmit image roles. Negative prompt, callback URL, and raw `content` items are also unavailable.

