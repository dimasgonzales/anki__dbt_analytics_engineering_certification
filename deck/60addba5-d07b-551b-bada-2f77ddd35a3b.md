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
  verdict: SUPPORTED
  explanation: "The Reference Text explicitly shows that configuration keys under 'seeds' require a '+' prefix, as demonstrated in examples where keys like 'schema' are prefixed with '+'. This supports the answer's claim that 'delimiter' should have '+' to avoid being interpreted as a subdirectory."
  citation:
    evidence_source: "https://docs.getdbt.com/reference/seed-configs"
    quote: "To apply a configuration to all seeds, including those in any installed packages, nest the configuration directly under the 'seeds' key: dbt_project.yml... seeds:... +schema: seed_data"
    is_quote_valid: true
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
