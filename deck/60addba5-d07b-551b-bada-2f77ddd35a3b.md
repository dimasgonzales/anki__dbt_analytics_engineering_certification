---
tags:
- seeds
- test-config
- yaml-compilation
citations:
- cleaned_docs/seeds/rank_4.md
guid: dbab72566f
source: llm
uuid: 60addba5-d07b-551b-bada-2f77ddd35a3b
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
