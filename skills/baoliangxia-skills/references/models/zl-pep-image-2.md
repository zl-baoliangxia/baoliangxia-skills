# Image 2 async

Use this reference for `zl-pep-image-2-async`. The upstream documentation calls it `gpt-image-2-async`; never send that upstream name as the baoliangxia `model` value.

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
| Output count | `--n N` | `1`–`10`; async upstream limit is 10 |
| Reference/edit images | repeat `--input-upload-id ID` | At most 3 in the current database configuration |

```bash
python3 {baseDir}/scripts/create_model_generation.py "改成电影概念设计风格" \
  --model zl-pep-image-2-async --aspect-ratio 16:9 --resolution 2K \
  --n 2 --input-upload-id upl_reference
```

baoliangxia returns a `generationId`; always use the shared query script.

## 不可用能力

The Gateway does not expose quality (`low`/`medium`/`high`/`auto`), background mode, response format, Base64-result selection, mask, callback URL, or the upstream `async` switch. Do not pass `gpt-image-2*` as the model identifier.

