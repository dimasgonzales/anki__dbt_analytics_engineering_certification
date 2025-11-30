---
tags:
- compiled-code
- error-logs
- yaml-compilation
citations:
- cleaned_docs/sources/rank_7.md
guid: fed2947c1c
source: llm
uuid: f5ac7b52-bd6c-573a-aa49-742bcab5bfa5
---

<front>

In the context of `sources.json`, what is the difference between a status of `error` and `runtime error`?

</front>

---

<back>

- **error**: The data is successfully queried but is stale (exceeded the `error_after` threshold).
- **runtime error**: The query failed to execute entirely (e.g., SQL syntax error, database permission issue, or table not found).

</back>
