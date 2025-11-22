---
tags:
  - selectors
  - compiled-code
  - modularity
citations:
  - https://docs.getdbt.com/reference/node-selection/exclude
guid: lVU,U#}/LW
source: apkg
uuid: ae30f94c-c7ae-55bd-8ecf-5378d08eac3e
---

<front>

how do you select the **set difference** of two selectors?

</front>

---

<back>

Using the `--exclude` CLI argument, which has the exact same semantics as `--select`. Basically, any nodes "selected" using the `--exclude` argument will be removed from the node set returned by the `--select` option.   
  
Example: `dbt run --select my_package.*+ --exclude my_package.a_big_model+`
  
  
Will select every model (and their children) from "my\_package" *except* for "my\_package.a\_big\_model" and *its* children.

</back>
