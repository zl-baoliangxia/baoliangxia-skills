# Wan 3.0 video family

Use this reference for `wan3.0-video` and `wan3.0-video-prime`. Prime uses the same parameters with a different exact database identifier.

## Script

```bash
python3 {baseDir}/scripts/create_model_generation.py "USER_PROMPT" \
  --model wan3.0-video [options]
```

## 参数拼装

Omitted `--aspect-ratio` becomes `adaptive`. Omitted `--resolution` becomes uppercase `1080P` for both `wan3.0-video` and `wan3.0-video-prime`. Both match the documented defaults. Explicit flags win.

| Intent | Flag | Rule |
|---|---|---|
| Output seconds | `--duration N` | `2`–`30`, or `-1` for adaptive duration |
| Aspect ratio | `--aspect-ratio VALUE` | `adaptive`, `9:16`, `16:9`, `4:3`, `3:4`, `1:1` |
| Resolution | `--resolution VALUE` | Exact uppercase values: `480P`, `720P`, `1080P` |
| Primary image | `--image-upload-id ID` | General driving image |
| Reference images | repeat `--reference-image-id ID` | At most 10 |
| Reference videos | repeat `--reference-video-id ID` | At most 5; total source duration ≤15 seconds |
| Reference audio | `--audio-upload-id ID` | One uploaded reference audio; total source duration ≤15 seconds |

When video input is present, input duration plus requested output duration must not exceed 30 seconds.

```bash
python3 {baseDir}/scripts/create_model_generation.py "参考运镜生成广告" \
  --model wan3.0-video-prime --duration 10 --resolution 1080P \
  --aspect-ratio 16:9 --reference-video-id upl_motion
```

## 不可用能力

The Gateway cannot select explicit first/last-frame roles, output-audio mode, seed, watermark, callback URL, provider `file`, or provider `link`.

