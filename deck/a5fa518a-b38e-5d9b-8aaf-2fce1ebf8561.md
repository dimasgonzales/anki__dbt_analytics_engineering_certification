---
tags:
- card_type/factual
- debugging/compiled-code
- debugging/error-logs
- debugging/yaml-compilation
citations:
- cleaned_docs/jinja-macros/rank_6.md
guid: 014e1c0c1d
source: llm
uuid: a5fa518a-b38e-5d9b-8aaf-2fce1ebf8561
---

<front>

What is the primary purpose of wrapping `run_query` calls within an `{% if execute %}` block in dbt Jinja?

</front>

---

<back>

It prevents the query from running during the **parsing phase**. Without it, dbt attempts to execute the query while compiling the project, which can cause compilation errors (e.g., if tables don't exist yet) or significantly slow down CLI commands.

</back>
