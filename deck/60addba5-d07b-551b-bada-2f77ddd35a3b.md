---
tags:
- card_type/factual
- debugging/yaml-compilation
- development/seeds
- testing/test-config
citations:
- cleaned_docs/seeds/rank_4.md
guid: dbab72566f
source: llm
uuid: 60addba5-d07b-551b-bada-2f77ddd35a3b
claim_meta:
  verdict: NOT_FOUND
  explanation: "The Reference Text discusses general errors and debugging in dbt_project.yml, such as unexpected keys and parsing issues, but does not mention the use of the '+' prefix for seeds configuration or address whether 'delimiter' requires it. Therefore, there is insufficient information to verify the answer."
  citation:
    quote: null
    is_quote_valid: false
---

<front>

You are troubleshooting a `dbt_project.yml` file where dbt seems to think your configuration key is a subdirectory name. What is the likely syntax error in the example below?

```yaml
seeds:
  delimiter: "|"
```

</front>

---

<back>

The configuration key is missing the `+` prefix. Without the `+`, dbt interprets `delimiter` as a folder name rather than a configuration setting.

Correction:
```yaml
seeds:
  +delimiter: "|"
```

</back>
