---
tags:
  - test-config
  - dbt-clone
  - project-config
citations:
- cleaned_docs/test-config/rank_2.md
guid: 313aed1557
source: llm
uuid: ce6efb9f-4089-5ca8-983d-edeabae2a042
---

<front>

How can you apply a configuration, such as `severity` or `enabled`, to all tests within a specific subdirectory using `dbt_project.yml`?

</front>

---

<back>

Define the configuration under the `data_tests` (or `tests`) key, specifying the project name and directory structure.

```yaml
data_tests:
  my_project:
    staging:
      +severity: warn
```

</back>
