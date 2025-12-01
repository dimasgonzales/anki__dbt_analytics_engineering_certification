---
tags:
- card_type/scenario
- contracts
- descriptions
- seeds
citations:
- cleaned_docs/descriptions/rank_2.md
guid: 657dc3fc1f
source: llm
uuid: d4e4e76f-cc6f-5ab2-ae55-7e649c92efcd
---

<front>

You need to add a description to a model that includes a 10-row markdown table and several paragraphs of text. How should you implement this in dbt?

</front>

---

<back>

Create a documentation block in a `.md` file for the content, then reference it in the `schema.yml` using the `doc()` function. Putting this much content directly in the YAML file would make it difficult to read and maintain.

Code:
```yaml
description: "{{ doc('complex_model_logic') }}"
```

</back>
