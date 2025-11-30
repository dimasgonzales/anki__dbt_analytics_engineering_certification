---
tags:
- descriptions
- modularity
- yaml-compilation
citations:
- cleaned_docs/sources/rank_6.md
guid: 5d15ea4f74
source: llm
uuid: a136a45b-5ddf-5872-9ada-fa4e4ff0a9fd
---

<front>

A developer receives a YAML parsing error for the following line: `description: Lists users [active only]`. What is the cause and how do you fix it?

</front>

---

<back>

The error is caused by the square brackets `[]`, which YAML interprets as an array definition. To fix it, wrap the entire string in quotes.

Corrected:
```yaml
description: "Lists users [active only]"
```

</back>
