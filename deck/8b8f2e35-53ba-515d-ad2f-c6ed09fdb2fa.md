---
tags:
- project-config
- snapshots
- yaml-compilation
citations:
- cleaned_docs/grants/rank_7.md
guid: ca4aa01595
source: llm
uuid: 8b8f2e35-53ba-515d-ad2f-c6ed09fdb2fa
---

<front>

Your BI tool cannot handle `NULL` values in the end-date column for active records. How do you configure a dbt snapshot to use '9999-12-31' instead of `NULL` for the current valid record?

</front>

---

<back>

Configure the `dbt_valid_to_current` setting in the snapshot config. This overrides the default `NULL` value with the specified SQL expression or static value.
```yaml
config:
  dbt_valid_to_current: "cast('9999-12-31' as date)"
```

</back>
