---
tags:
- card_type/factual
- development/modularity
- development/python-models
- development/snapshots
citations:
- cleaned_docs/error-logs/rank_2.md
guid: 2e09257181
source: llm
uuid: 2bac085c-fec7-5c86-8bb5-7c81dc9dafd2
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly states that for events related to specific nodes, the 'data' key contains a 'node_info' dictionary with common attributes, which supports the answer that 'node_info' provides configuration details such as materialization strategy and unique ID."
  citation:
    quote: "If this event relates to a specific node within your dbt project, it will contain a `node_info` dictionary with common attributes."
    is_quote_valid: true
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
