---
tags:
- card_type/factual
- debugging/compiled-code
- documentation/descriptions
- documentation/docs-generation
citations:
- cleaned_docs/packages/rank_9.md
guid: 835a0fc5a6
source: llm
uuid: fc49bcce-e71a-5fbc-a197-7bc98439fa7d
claim_meta:
  verdict: NOT_FOUND
  explanation: "The reference text does not mention the 'dbt docs generate' command or its interaction with the '--select' flag, so it cannot be verified."
  citation:
    quote: null
    is_quote_valid: false
---

<front>

What is the result of using the `--select` flag with the `dbt docs generate` command?

</front>

---

<back>

It generates a **partial** `catalog.json` containing metadata only for the selected subset of resources. This significantly reduces the runtime by avoiding expensive warehouse metadata queries for the entire project.

</back>
