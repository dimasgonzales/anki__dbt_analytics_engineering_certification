---
uuid: a0dfab8f-5a9d-4ef3-8ed5-d16c5e05ecd8
guid: B_!t!w|{N$
tags:
  - node_selection
citations:
  - https://docs.getdbt.com/reference/node-selection/syntax
---

<front>
What is the "order of operations" for dbt node selection?
</front>

---

<back>

1. dbt gathers all the resources that are matched by one or more of the `--select` criteria, in the order of selection methods (e.g. `tag:`), then graph operators (e.g. `+`), then finally set operators (unions, intersections, exclusions).
2. The selected resources may be models, sources, seeds, snapshots, tests. (Tests can also be selected "indirectly" via their parents)
3. dbt now has a list of still-selected resources of varying types. As a final step, it tosses away any resource that does not match the resource type of the current task. (Only seeds are kept for `dbt seed`, only models for `dbt run`, only tests for `dbt test`, and so on.)

</back>
