---
tags:
- card_type/factual
- development/materializations
- development/modularity
- development/packages
citations:
- cleaned_docs/docs-generation/rank_7.md
guid: 1a1365c5d7
source: llm
uuid: fe7f36e9-b04c-5460-acbc-0beebea0ebec
---

<front>

What is the primary purpose of the `dbt_utils.star` macro?

</front>

---

<back>

The `dbt_utils.star` macro generates a comma-separated list of all fields from a relation (table or view). It is primarily used to select all columns while allowing for the exclusion of specific columns via the `except` argument, promoting DRY code conventions.

</back>
