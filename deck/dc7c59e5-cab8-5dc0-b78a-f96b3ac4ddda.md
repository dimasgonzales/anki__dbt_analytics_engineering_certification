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
---

<front>

When using Extended Attributes to modify configuration in dbt Cloud, what is the critical constraint regarding sub-keys (nested fields)?

</front>

---

<back>

Extended attributes perform a **top-level key replacement**. They do not merge sub-keys. If you need to modify a value inside a nested object (like a specific field in a JSON keyfile), you must provide the *entire* top-level key block.

</back>
