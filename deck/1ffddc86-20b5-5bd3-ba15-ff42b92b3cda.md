---
tags:
- card_type/factual
- modularity
- project-config
- yaml-compilation
citations:
- cleaned_docs/yaml-compilation/rank_1.md
guid: 3017dbf5d7
source: llm
uuid: 1ffddc86-20b5-5bd3-ba15-ff42b92b3cda
---

<front>

What is the strict indentation rule for dbt YAML files, and which character causes immediate parsing errors?

</front>

---

<back>

dbt YAML files require **space-based** indentation. The use of **tab characters** is forbidden and will cause a `Could not parse dbt_project.yml` error during the compilation phase.

</back>
