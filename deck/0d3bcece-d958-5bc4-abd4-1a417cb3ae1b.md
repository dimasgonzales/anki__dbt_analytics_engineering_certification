---
tags:
  - python-models
  - test-config
  - jinja-macros
citations:
- cleaned_docs/python-models/rank_4.md
guid: bd315e6fb7
source: llm
uuid: 0d3bcece-d958-5bc4-abd4-1a417cb3ae1b
---

<front>

What is the performance difference between using standard `pandas` DataFrames and native DataFrames (like Snowpark or PySpark) in dbt?

</front>

---

<back>

Native DataFrames support **lazy evaluation** and **distributed processing**, pushing computation down to the data warehouse (Snowflake/Databricks). Standard `pandas` DataFrames pull data into memory on a single node, which can lead to performance bottlenecks or memory errors with large datasets.

</back>
