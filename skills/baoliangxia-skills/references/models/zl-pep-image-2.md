# Image 2 async

Use this reference for `zl-pep-image-2-async`, `zl-pep-image-2.5-flare-async`, and `zl-pep-image-2.5-sunburst-async`. The upstream documentation calls these `gpt-image-2*`; never send an upstream name as the baoliangxia `model` value.

All three default to `16:9` and `1K`. The 2.5 flare and sunburst identifiers create one output per task; the original 2 async model supports up to 10.

## Script

```bash
python3 {baseDir}/scripts/create_model_generation.py "USER_PROMPT" \
  --model zl-pep-image-2-async [options]
```

## 参数拼装

Omitted `--aspect-ratio` becomes `16:9`. Omitted `--resolution` becomes `1K`, the tier nearest 720p. Explicit flags win.

| Intent | Flag | Rule |
|---|---|---|
| Aspect ratio | `--aspect-ratio VALUE` | Supports `1:1`, `1:2`, `1:3`, `2:1`, `2:3`, `3:1`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `16:9`, `21:9`, `9:16`, `9:21` |
| Resolution tier | `--resolution VALUE` | `1K`, `2K`, or `4K`; the Gateway resolves it with the ratio to an exact pixel size |
| Quality | `--option quality=VALUE` | `auto`, `low`, `medium`, `high`; defaults to `auto` |
| Background | `--option background=VALUE` | `auto` or `opaque`; defaults to `auto` |
| Watermark | — | Not exposed for Image 2 |
| Output count | `--n N` | `1`–`10`; async upstream limit is 10 |
| Reference/edit images | repeat `--input-upload-id ID` | At most 3 in the current database configuration |

```bash
python3 {baseDir}/scripts/create_model_generation.py "改成电影概念设计风格" \
  --model zl-pep-image-2-async --aspect-ratio 16:9 --resolution 2K \
  --n 2 --input-upload-id upl_reference
```

baoliangxia returns a `generationId`; always use the shared query script.

## 不可用能力

Quality and background are Gateway options on all three listed identifiers. The two 2.5 identifiers are exposed through this skill catalog; availability still depends on the Gateway model being enabled. Response format, Base64-result selection, mask, callback URL, and the upstream `async` switch are unavailable. Do not pass `gpt-image-2*` as the model identifier.

