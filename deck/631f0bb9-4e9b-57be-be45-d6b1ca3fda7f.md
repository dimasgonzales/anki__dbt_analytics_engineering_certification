---
tags:
- modularity
- sql-performance
- test-types
citations:
- cleaned_docs/docs-generation/rank_5.md
guid: f70b5c9a90
source: llm
uuid: 631f0bb9-4e9b-57be-be45-d6b1ca3fda7f
---

<front>

What are the two main risks of creating a composite key using simple concatenation without separators or null handling?

</front>

---

<back>

1. **Null Propagation:** In most databases, if one column is `null`, the entire result becomes `null`.
2. **Collisions:** Without separators, different value combinations can result in the same string (e.g., '1' + '11' is the same as '11' + '1').

</back>
