---
tags:
- card_type/factual
- debugging/yaml-compilation
- development/project-config
- pipelines/deployment-jobs
citations:
- cleaned_docs/deployment-jobs/rank_4.md
guid: e1a6ea9004
source: llm
uuid: dc7c59e5-cab8-5dc0-b78a-f96b3ac4ddda
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly states that extended attributes only accept top-level keys and do not merge sub-keys, confirming that to modify a nested field, the entire top-level key must be provided."
  citation:
    quote: "Only the **top-level keys** are accepted in extended attributes. This means that if you want to change a specific sub-key value, you must provide the entire top-level key as a JSON block in your resulting YAML."
    is_quote_valid: false
---

<front>

When using Extended Attributes to modify configuration in dbt Cloud, what is the critical constraint regarding sub-keys (nested fields)?

</front>

---

<back>

Extended attributes perform a **top-level key replacement**. They do not merge sub-keys. If you need to modify a value inside a nested object (like a specific field in a JSON keyfile), you must provide the *entire* top-level key block.

</back>
