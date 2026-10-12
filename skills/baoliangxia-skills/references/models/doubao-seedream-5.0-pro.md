# `doubao-seedream-5.0-pro`

Always submit `doubao-seedream-5.0-pro`; do not replace it with a display name.

## Script

```bash
python3 {baseDir}/scripts/create_model_generation.py "USER_PROMPT" \
  --model doubao-seedream-5.0-pro [options]
```

## 参数拼装

Omitted `--aspect-ratio` becomes `1:1`. Omitted `--resolution` becomes `2K`, matching the documented size default `2048x2048`. Explicit flags win.

| Intent | Flag | Rule |
|---|---|---|
| Aspect ratio | `--aspect-ratio VALUE` | `9:16`, `16:9`, `3:4`, `4:3`, `1:1`, `3:2`, `2:3`, `21:9` |
| Resolution | `--resolution VALUE` | Database-exposed tiers: `1K` or `2K` |
| Output format | `--output-format png|jpeg` | Omit unless requested |
| Reference/edit images | repeat `--input-upload-id ID` | At most 10 |

```bash
python3 {baseDir}/scripts/create_model_generation.py "商品主图，白色背景" \
  --model doubao-seedream-5.0-pro --aspect-ratio 1:1 --resolution 2K \
  --input-upload-id upl_product
```

## 不可用能力

The Gateway does not expose `layer_decomposition`, exact pixel size, `1.5K`, prompt optimization controls, response format, watermark, web search, streaming, or output count. Do not pass `--n` for this model.

