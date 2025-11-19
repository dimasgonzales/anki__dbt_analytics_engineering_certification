---
uuid: c2cf57b6-dc93-44ff-a0ae-22de914acd2c
guid: pj!J/>e{%Y
tags:
  - dbt_commands
citations:
  - https://docs.getdbt.com/reference/commands/build
---

<front>
What does the `dbt build` command do?
</front>

---

<back>

The `dbt build` command will:

- run models
- test tests
- snapshot snapshots
- seed seeds

In DAG order, for selected resources or an entire project.

You can build a subset of resources using standard selection syntax, plus `--resource-type` flag that offers a final filter layer (e.g. restrict build to just snapshots). In general, the build task supports the same flags as run, test, snapshot, and seed.

The build task will also write a single manifest file and a single run results artifact, which contains the run results for all models, tests, seeds, etc., combined into one file.

</back>
