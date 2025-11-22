---
tags:
  - yaml-compilation
  - materializations
  - cli-commands
citations:
- cleaned_docs/model-access/rank_8.md
guid: 723d065cd0
source: llm
uuid: 73bf5ea7-e7ab-5efc-81fd-0859f79caada
---

<front>

How do you distinguish between a model-level test and a column-level test in a dbt YAML file?

</front>

---

<back>

By indentation and hierarchy:

1. **Model-level tests** are defined directly under the model's `data_tests` key (validating the whole table).
2. **Column-level tests** are nested under a specific column's `data_tests` key within the `columns` list.

</back>
