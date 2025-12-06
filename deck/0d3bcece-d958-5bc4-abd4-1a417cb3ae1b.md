---
tags:
- card_type/factual
- development/jinja-macros
- development/python-models
- testing/test-config
citations:
- cleaned_docs/python-models/rank_4.md
guid: bd315e6fb7
source: llm
uuid: 0d3bcece-d958-5bc4-abd4-1a417cb3ae1b
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly states that pandas DataFrames operate on a single node without distributed computing benefits, while native DataFrames like PySpark leverage parallel processing, supporting the performance differences described in the answer."
  citation:
    quote: "pandas runs \"single-node\" transformations, which cannot benefit from the parallelism and distributed computing offered by modern data warehouses."
    is_quote_valid: true
---

<front>

What is the performance difference between using standard `pandas` DataFrames and native DataFrames (like Snowpark or PySpark) in dbt?

</front>

---

<back>

Native DataFrames support **lazy evaluation** and **distributed processing**, pushing computation down to the data warehouse (Snowflake/Databricks). Standard `pandas` DataFrames pull data into memory on a single node, which can lead to performance bottlenecks or memory errors with large datasets.

</back>
