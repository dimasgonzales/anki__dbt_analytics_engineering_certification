---
tags:
- card_type/factual
- development/jinja-macros
- development/python-models
- documentation/docs-generation
citations:
- cleaned_docs/jinja-macros/rank_9.md
guid: e491540a24
source: llm
uuid: 1eb6b7c5-c8a6-51eb-aafa-f6a05619fec0
---

<front>

In a dbt macro, what is the primary data type difference between using the `return` function versus standard Jinja output capture?

</front>

---

<back>

The `return` function preserves the **Python data type** (e.g., lists, dictionaries, integers) of the argument. 

Standard Jinja capture (printing to the template) converts the output into a **string**.

</back>
