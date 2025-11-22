---
tags:
  - cli-commands
  - project-config
  - selectors
citations:
- cleaned_docs/project-config/rank_7.md
guid: 359019d817
source: llm
uuid: b8e36f4b-fe6d-580c-afaf-dde8fcbae1a3
---

<front>

Which keys in `dbt_project.yml` represent the configuration for overriding default directory locations for models, seeds, and tests?

</front>

---

<back>

The keys are `model-paths`, `seed-paths`, and `test-paths` (note the plural 'paths'). These accept lists of directory strings.

```yaml
model-paths: ["models"]
seed-paths: ["seeds"]
```

</back>
