# `zl-ooe-3.1-flash-image-t`

baoliangxia requests must use the database identifier `zl-ooe-3.1-flash-image-t`.

## Script

```bash
python3 {baseDir}/scripts/create_model_generation.py "USER_PROMPT" \
  --model zl-ooe-3.1-flash-image-t [options]
```

## 参数拼装

Omitted `--aspect-ratio` becomes `16:9`. This model has no Gateway resolution field, so do not send `--resolution`.

| Intent | Flag | Rule |
|---|---|---|
| Aspect ratio | `--aspect-ratio VALUE` | `1:1`, `3:4`, `4:3`, `16:9`, `9:16`, `21:9`, `3:2`, `2:3`, `5:4`, `4:5` |
| Reference/edit images | repeat `--input-upload-id ID` | At most 3 in the current model configuration |

```bash
python3 {baseDir}/scripts/create_model_generation.py "把背景改成海边日落" \
  --model zl-ooe-3.1-flash-image-t --aspect-ratio 16:9 \
  --input-upload-id upl_reference
```

## 不可用能力

`--option imageSize=1K|2K|4K` selects the image size; it defaults to `2K`. Do not pass `--resolution`, output count, output format, response modality, or a raw provider `contents` payload. Watermark is not exposed for this model.
