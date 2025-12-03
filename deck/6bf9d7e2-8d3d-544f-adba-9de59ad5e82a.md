---
tags:
- card_type/factual
- development/jinja-macros
citations:
- cleaned_docs/packages/rank_6.md
guid: c899969a7b
source: llm
uuid: 6bf9d7e2-8d3d-544f-adba-9de59ad5e82a
---

<front>

What macro allows a dbt package to execute different SQL logic dynamically based on the active warehouse adapter (e.g., Snowflake vs. BigQuery)?

</front>

---

<back>

The `adapter.dispatch` macro.

It looks up the macro implementation specific to the current adapter (e.g., `spark__my_macro`) and falls back to the default implementation if a specific one isn't found.

Example:
```jinja
{{ adapter.dispatch('my_macro')() }}
```

</back>
