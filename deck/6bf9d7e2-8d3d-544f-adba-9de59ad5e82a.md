---
tags:
- card_type/factual
- development/jinja-macros
citations:
- cleaned_docs/packages/rank_6.md
guid: c899969a7b
source: llm
uuid: 6bf9d7e2-8d3d-544f-adba-9de59ad5e82a
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly states that the `adapter.dispatch` macro is used to implement cross-database compatibility for macros in dbt, which aligns with executing different SQL logic dynamically based on the active warehouse adapter."
  citation:
    quote: "If you need to implement cross-database compatibility for one of your macros, use the [`adapter.dispatch` macro](/reference/dbt-jinja-functions/dispatch) to achieve this."
    is_quote_valid: true
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
