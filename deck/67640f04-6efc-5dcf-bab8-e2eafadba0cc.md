---
tags:
  - project-config
  - sources
  - materializations
citations:
- cleaned_docs/sources/rank_10.md
guid: c73ae837fe
source: llm
uuid: 67640f04-6efc-5dcf-bab8-e2eafadba0cc
---

<front>

You want to apply a specific configuration to all source tables in your project. You attempt to add a `sources:` block to your `dbt_project.yml` file. Will this work?

</front>

---

<back>

No, this will not work. Source configurations must be defined in `.yml` files within the `models/` directory. The `dbt_project.yml` file is used for project-level configurations (like model hierarchies), but sources are exclusively defined in their own YAML files.

</back>
