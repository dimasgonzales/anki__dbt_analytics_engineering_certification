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
claim_meta:
  verdict: SUPPORTED
  explanation: "The Reference Text provides evidence that the `return` function in dbt macros preserves Python data types, as shown in examples where it returns a list without converting to a string, allowing direct use in Jinja contexts. This supports the answer's claim that `return` preserves data types, while standard Jinja output implicitly converts to string."
  citation:
    quote: "getdata() returns a list!"
    is_quote_valid: true
---

<front>

In a dbt macro, what is the primary data type difference between using the `return` function versus standard Jinja output capture?

</front>

---

<back>

The `return` function preserves the **Python data type** (e.g., lists, dictionaries, integers) of the argument. 

Standard Jinja capture (printing to the template) converts the output into a **string**.

</back>
