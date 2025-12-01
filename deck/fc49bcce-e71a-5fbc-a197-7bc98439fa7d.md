---
tags:
- card_type/factual
- compiled-code
- descriptions
- docs-generation
citations:
- cleaned_docs/packages/rank_9.md
guid: 835a0fc5a6
source: llm
uuid: fc49bcce-e71a-5fbc-a197-7bc98439fa7d
---

<front>

What is the result of using the `--select` flag with the `dbt docs generate` command?

</front>

---

<back>

It generates a **partial** `catalog.json` containing metadata only for the selected subset of resources. This significantly reduces the runtime by avoiding expensive warehouse metadata queries for the entire project.

</back>
