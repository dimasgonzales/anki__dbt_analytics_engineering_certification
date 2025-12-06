---
citations:
- cleaned_docs/python-models/rank_9.md
tags:
- card_type/factual
- development/project-config
- development/sources
uuid: 5b829eb5-dec9-589d-adbd-08c0ea52af4e
claim_meta:
  verdict: CONTRADICTED
  explanation: "The answer omits the 'Properties defined in a .yml file' as a precedence level, which is explicitly included in the reference text as the second highest priority."
  citation:
    evidence_source: "https://docs.getdbt.com/reference/define-configs"
    quote: "The precedence order is as follows: 1. In-file config() block, 2. Properties defined in a .yml file, 3. Config defined in the project file."
    is_quote_valid: false
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