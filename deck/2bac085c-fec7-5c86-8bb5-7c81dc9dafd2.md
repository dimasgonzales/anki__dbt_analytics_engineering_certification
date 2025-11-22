---
tags:
  - python-models
  - snapshots
  - modularity
citations:
- cleaned_docs/error-logs/rank_2.md
guid: 2e09257181
source: llm
uuid: 2bac085c-fec7-5c86-8bb5-7c81dc9dafd2
---

<front>

Which nested object within the `data` key of a dbt log event provides configuration details such as the materialization strategy and unique ID?

</front>

---

<back>

The `node_info` object.

It provides specific context about the DAG node being processed:
```json
"node_info": {
  "materialized": "view",
  "unique_id": "model.my_project.my_model"
}
```

</back>
