---
tags:
- card_type/factual
- development/modularity
- development/sql-performance
- testing/test-types
citations:
- cleaned_docs/docs-generation/rank_5.md
guid: f70b5c9a90
source: llm
uuid: 631f0bb9-4e9b-57be-be45-d6b1ca3fda7f
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly supports both risks: it states that null values in concatenation often cause the entire result to be null, and it notes that ignoring nulls can lead to collisions where different inputs produce the same key. For example, it mentions that with certain concatenation methods, nulls propagate to null results, and that handling nulls improperly can result in identical keys from different value combinations."
  citation:
    quote: "If any value is null, then often the entire concatenated string is returned as null"
    is_quote_valid: true
---

<front>

What are the two main risks of creating a composite key using simple concatenation without separators or null handling?

</front>

---

<back>

1. **Null Propagation:** In most databases, if one column is `null`, the entire result becomes `null`.
2. **Collisions:** Without separators, different value combinations can result in the same string (e.g., '1' + '11' is the same as '11' + '1').

</back>
