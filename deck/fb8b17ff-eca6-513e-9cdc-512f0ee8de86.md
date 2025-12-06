---
tags:
- card_type/scenario
- development/modularity
- development/seeds
- development/snapshots
citations:
  - docs/site_docs.getdbt.com/citations/docs_getdbt_com_reference_dbt_jinja_functions_adapter.md
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
