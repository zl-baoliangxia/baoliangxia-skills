# `doubao-seedream-4.5`

Read this file only after selecting the exact model `doubao-seedream-4.5`.

## Script

```bash
python3 {baseDir}/scripts/create_model_generation.py "USER_PROMPT" \
  --model doubao-seedream-4.5 [options]
```

The script hardcodes the model. Omitted `--aspect-ratio` becomes `1:1` and omitted `--resolution` becomes `2K`, matching the documented size default `2048x2048`. Explicit flags win. Other omitted optional fields stay omitted.

## 参数拼装

| User intent or available input | Script flag | Gateway field | Rule |
|---|---|---|---|
| Always | positional prompt | `prompt` | Preserve the user's text |
| User specifies a supported ratio | `--aspect-ratio VALUE` | `aspectRatio` | `1:1`, `4:3`, `3:4`, `16:9`, `9:16`, `3:2`, `2:3`, or `21:9` |
| User specifies resolution tier | `--resolution VALUE` | `resolution` | Exact value: `2K` or `4K`; `3K` is invalid |
| User specifies output count | `--n N` | `n` | `1` through `15`, also obey combined limit below |
| Reference/edit images exist | repeat `--input-upload-id ID` | `inputImages` | At most 14 references |

Reference image count plus requested output count must not exceed 15. If `--n` is absent, count one output.

```bash
python3 {baseDir}/scripts/create_model_generation.py "生成竖版商品海报" \
  --model doubao-seedream-4.5 \
  --aspect-ratio 3:4 --resolution 4K --input-upload-id upl_product
```

## 不可用能力

The Gateway translates `n` to the group-image limit and, when n is explicit, selects `auto` for multiple images or `disabled` for one. Actual output count may be lower than n. For multiple images, use `create_batch_generations.py --count N` to wait and request only the remaining count. Reference slots reduce the per-request limit. Raw group-image controls, streaming, `response_format`, `watermark`, prompt optimization, and web search are not exposed.

Do not send `outputFormat`: the source document marks `output_format` as a `doubao-seedream-5.0-lite`-only field.
