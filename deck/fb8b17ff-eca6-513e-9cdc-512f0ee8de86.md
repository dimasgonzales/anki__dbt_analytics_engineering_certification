---
tags:
  - seeds
  - snapshots
  - modularity
citations:
  - https://docs.getdbt.com/reference/dbt-jinja-functions/adapter
guid: LNbCu:E4is
source: apkg
uuid: fb8b17ff-eca6-513e-9cdc-512f0ee8de86
---

<front>

How can you check if a relation exists in your database?

</front>

---

<back>

Using the `adapter.load_relation` method.   
  
Example:
  

```
{% set relation_exists = (adapter.load_relation(ref('my_model')) is not none %}
```

</back>
