---
uuid: 4dff8d18-347b-4c8c-b190-afaf2fa5e2ca
guid: NV}Y+d8A_j
tags:
  - resource_configs
citations:
  - https://docs.getdbt.com/reference/resource-configs/sql_header
---

<front>
What does the `sql_header` model config do, and how does it differ from `pre_hook`?
</front>

---

<back>

`sql_header` allows you to specify some SQL that will be executed just before the model creation statement, *as part of the same query*. This is distinct from `pre_hook`, which executes statements in a *preceding* query.

</back>
