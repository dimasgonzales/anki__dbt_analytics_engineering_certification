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
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly advises wrapping logic in an if execute block to avoid issues during parsing, which directly supports the answer's claim about preventing query execution during the parsing phase."
  citation:
    quote: "Make sure to wrap the logic in an [if execute](/reference/dbt-jinja-functions/execute) block to avoid unexpected behavior during parsing."
    is_quote_valid: true
---

<front>

What is the primary purpose of wrapping `run_query` calls within an `{% if execute %}` block in dbt Jinja?

</front>

---

<back>

It prevents the query from running during the **parsing phase**. Without it, dbt attempts to execute the query while compiling the project, which can cause compilation errors (e.g., if tables don't exist yet) or significantly slow down CLI commands.

</back>
