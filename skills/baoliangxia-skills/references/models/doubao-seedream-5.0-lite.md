# `doubao-seedream-5.0-lite`

Read this file only after selecting the exact model `doubao-seedream-5.0-lite`.

## Script

```bash
python3 {baseDir}/scripts/create_model_generation.py "USER_PROMPT" \
  --model doubao-seedream-5.0-lite [options]
```

The script hardcodes the model. Omitted `--aspect-ratio` becomes `1:1` and omitted `--resolution` becomes `2K`, matching the documented size default `2048x2048`. Explicit flags win. Other omitted optional fields stay omitted.

## 参数拼装

| User intent or available input | Script flag | Gateway field | Rule |
|---|---|---|---|
| Always | positional prompt | `prompt` | Preserve the user's text |
| User specifies a supported ratio | `--aspect-ratio VALUE` | `aspectRatio` | `1:1`, `4:3`, `3:4`, `16:9`, `9:16`, `3:2`, `2:3`, or `21:9` |
| User specifies resolution tier | `--resolution VALUE` | `resolution` | Exact value: `2K`, `3K`, or `4K` |
| User specifies output count | `--n N` | `n` | `1` through `15`, also obey combined limit below |
| User explicitly requests PNG or JPEG | `--output-format png|jpeg` | `outputFormat` | Omit when the user does not choose a format |
| Reference/edit images exist | repeat `--input-upload-id ID` | `inputImages` | At most 14 references |

Reference image count plus requested output count must not exceed 15. If `--n` is absent, count one output.

```bash
python3 {baseDir}/scripts/create_model_generation.py "生成三张商品场景图" \
  --model doubao-seedream-5.0-lite \
  --aspect-ratio 16:9 --resolution 3K --n 3 --output-format png \
  --input-upload-id upl_product
```

## 不可用能力

The upstream model supports `tools: [{"type":"web_search"}]`, but the current Agent Gateway rejects that field. If web search is required, stop before submission and report the missing Gateway capability.

Group-image mode, streaming, `response_format`, `watermark`, and prompt optimization are also not exposed. Do not place them in metadata.
