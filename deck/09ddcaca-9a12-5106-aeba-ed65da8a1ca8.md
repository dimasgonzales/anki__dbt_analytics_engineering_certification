---
tags:
- card_type/scenario
- compiled-code
- descriptions
- python-models
citations:
- cleaned_docs/materializations/rank_4.md
guid: 352a834e84
source: llm
uuid: 09ddcaca-9a12-5106-aeba-ed65da8a1ca8
---

<front>

You are debugging a custom materialization that runs successfully but causes dbt to trigger unnecessary metadata queries (like `show tables`) for downstream models. What specific step is missing in your materialization code?

</front>

---

<back>

The materialization is missing the **return statement** that updates the cache.

You need to add `{{ return({'relations': [target_relation]}) }}` so dbt knows the object exists without querying the database again.

</back>
