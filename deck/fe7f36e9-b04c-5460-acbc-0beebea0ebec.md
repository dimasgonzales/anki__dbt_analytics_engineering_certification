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
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly confirms that the dbt_utils.star macro generates a comma-separated list of all fields from a relation, allows exclusion of specific columns via the 'except' argument, and is used to write DRY code, which fully supports the answer."
  citation:
    quote: "Generates a comma-separated list of all fields that exist in the `from` [relation](https://docs.getdbt.com/reference/dbt-classes#relation) and excludes any fields listed in an `except` argument,"
    is_quote_valid: true
---

<front>

What is the primary purpose of the `dbt_utils.star` macro?

</front>

---

<back>

The `dbt_utils.star` macro generates a comma-separated list of all fields from a relation (table or view). It is primarily used to select all columns while allowing for the exclusion of specific columns via the `except` argument, promoting DRY code conventions.

</back>
