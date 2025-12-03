---
tags:
- card_type/scenario
- debugging/compiled-code
- development/python-models
- pipelines/dag-failures
citations:
- cleaned_docs/python-models/rank_1.md
guid: 6579eac895
source: llm
uuid: b6adefc3-8bc8-5d28-8c8e-b772f3caf0e3
---

<front>

Your Python model requires the `scikit-learn` library to run on Snowflake. How do you configure this dependency in the model file?

</front>

---

<back>

Use `dbt.config` to set the `packages` key with a list of required libraries.

```python
def model(dbt, session):
    dbt.config(packages=['scikit-learn'])
    # ...
```

</back>
