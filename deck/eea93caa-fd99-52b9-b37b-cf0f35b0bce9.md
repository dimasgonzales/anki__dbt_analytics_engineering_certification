---
tags:
- card_type/factual
- development/sources
- documentation/exposures
- documentation/lineage
citations:
- cleaned_docs/lineage/rank_4.md
guid: 3ecdd3a1d3
source: llm
uuid: eea93caa-fd99-52b9-b37b-cf0f35b0bce9
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly supports the answer by stating that column-level lineage helps understand precisely how data is used in models, facilitating debugging, which aligns with tracing specific fields and impact analysis."
  citation:
    quote: "the column level relationships help you understand *precisely* how data is used in models — this makes debugging data issues a lot simpler!"
    is_quote_valid: true
---

<front>

What is the primary benefit of 'Column-Level Lineage' over standard table-level lineage in dbt?

</front>

---

<back>

Column-Level Lineage allows you to trace specific fields (such as PII or primary keys) from their source all the way to downstream exposures. This is essential for auditing data usage and conducting precise impact analysis when a specific column's logic changes.

</back>
