---
tags:
- card_type/factual
- development/project-config
- development/sources
citations:
- cleaned_docs/python-models/rank_9.md
guid: 1f5bd196b7
source: llm
uuid: 5b829eb5-dec9-589d-adbd-08c0ea52af4e
---

<front>

In dbt, what is the order of precedence for model configurations (from highest priority to lowest) when defined in multiple locations?

</front>

---

<back>

1. **In-file config:** `{{ config() }}` block within the model `.sql` file (Highest/Winner).
2. **Project Subdirectory:** Configurations in `dbt_project.yml` applied to a specific folder.
3. **Project Global:** General configurations in `dbt_project.yml` (Lowest).

*Specific always overrides general.*

</back>
