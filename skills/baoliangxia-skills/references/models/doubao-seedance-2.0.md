# Seedance 2.0 family

Use this reference for `doubao-seedance-2.0`, `doubao-seedance-2.0-fast`, or `doubao-seedance-2.0-mini`. Always pass the exact selected database identifier.

## Script

```bash
python3 {baseDir}/scripts/create_model_generation.py "USER_PROMPT" \
  --model doubao-seedance-2.0 [options]
```

## 参数拼装

Omitted `--aspect-ratio` becomes `16:9`. Omitted `--resolution` becomes `720p` for `doubao-seedance-2.0`, `doubao-seedance-2.0-fast`, and `doubao-seedance-2.0-mini`. Explicit flags win.

| Intent | Flag | Rule |
|---|---|---|
| Output seconds | `--duration N` | Positive integer |
| Aspect ratio | `--aspect-ratio VALUE` | `9:16`, `16:9`, `3:4`, `4:3`, or `1:1` |
| Resolution | `--resolution VALUE` | Standard: `480p`/`720p`/`1080p`; fast/mini: `480p`/`720p` |
| Primary image | `--image-upload-id ID` | General driving image; not an explicit frame role |
| Reference images | repeat `--reference-image-id ID` | Upload first |
| Reference videos | repeat `--reference-video-id ID` | Upload first; total source duration ≤15 seconds |
| Reference audio | `--audio-upload-id ID` | Requires at least one image or video |

```bash
python3 {baseDir}/scripts/create_model_generation.py "产品缓慢旋转" \
  --model doubao-seedance-2.0-fast --resolution 720p \
  --aspect-ratio 16:9 --duration 8 --reference-image-id upl_product
```

## 不可用能力

The Gateway cannot select explicit first/last-frame roles, `generate_audio`, watermark, seed, callback URL, or the provider's extra tool fields. Do not emulate those fields through metadata.

