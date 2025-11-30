---
tags:
- descriptions
- exposures
- sources
citations:
- cleaned_docs/exposures/rank_3.md
guid: 698052df2d
source: llm
uuid: 0ab8f44c-a1cb-5d83-bfda-38bb2dc0a2ab
---

<front>

What specific metadata fields are used in an exposure to document the external resource's location and point of contact?

</front>

---

<back>

You use the `url` field to provide a link to the resource and the `owner` object (containing `name` and `email`) to specify the contact person.

```yaml
url: https://bi.tool.com/reports/123
owner:
  name: Finance Team
  email: finance@company.com
```

</back>
