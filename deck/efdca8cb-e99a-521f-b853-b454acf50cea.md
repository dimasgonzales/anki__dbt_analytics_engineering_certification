---
tags:
- card_type/factual
- debugging/compiled-code
- documentation/docs-generation
- state/state-concepts
citations:
- cleaned_docs/cli-commands/rank_7.md
guid: 0fb2cdc80e
source: llm
uuid: efdca8cb-e99a-521f-b853-b454acf50cea
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly states that the `--empty-catalog` flag skips database queries to populate `catalog.json`, making documentation generation faster and omitting database metadata such as column types and statistics, which directly supports the answer."
  citation:
    quote: "Use the `--empty-catalog` argument to skip running the database queries to populate `catalog.json`. ... It can speed up `docs generate` in development, as it means that your documentation will be missing information gleaned from database metadata (the full set of columns in each table, and statistics about those tables)."
    is_quote_valid: false
---

<front>

What is the purpose of the `--empty-catalog` flag when running `dbt docs generate`?

</front>

---

<back>

It instructs dbt to generate the documentation artifacts (index.html and manifest.json) but skip the expensive database queries required to build `catalog.json`. This makes generation significantly faster but omits database-specific details like column types.

</back>
