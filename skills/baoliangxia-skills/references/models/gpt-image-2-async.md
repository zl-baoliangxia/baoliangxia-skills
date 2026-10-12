# Legacy upstream name: `gpt-image-2-async`

This file is kept only as a compatibility pointer for older Skill installations. The enabled database identifier is `zl-pep-image-2-async`; never submit `gpt-image-2-async` as the model.

Read `references/models/zl-pep-image-2.md` for the current parameter rules and examples.

## 参数拼装

Use the exact database identifier with the unified script:

```bash
python3 {baseDir}/scripts/create_model_generation.py "USER_PROMPT" \
  --model zl-pep-image-2-async [options]
```

## 不可用能力

The upstream alias cannot be used as the request model identifier. All other capability limits are documented in `references/models/zl-pep-image-2.md`.
