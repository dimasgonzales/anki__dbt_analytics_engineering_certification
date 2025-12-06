---
citations:
- cleaned_docs/python-models/rank_9.md
tags:
- card_type/factual
- development/project-config
- development/sources
uuid: 5b829eb5-dec9-589d-adbd-08c0ea52af4e
claim_meta:
  verdict: SUPPORTED
  explanation: "The answer correctly lists the order of precedence for model configurations in dbt from highest to lowest: in-file config, properties file (.yml), and project config (dbt_project.yml). The reference text confirms this hierarchy and explicitly states that the most specific configuration takes precedence, following the same order."
  citation:
    evidence_source: "https://docs.getdbt.com/reference/define-configs"
    quote: "The most specific config always takes precedence. This generally follows the order above: an in-file `config()` block --> properties defined in a `.yml` file --> config defined in the project file."
    is_quote_valid: true
---


<front>

In dbt, what is the order of precedence for model configurations (from highest priority to lowest) when defined in multiple locations?

</front>

---

<back>

1. **In-file config**: `{{ config() }}` block in the .sql file.
2. **Properties file**: Configs defined in a .yml file. (e.g.: like the model yml)
3. **Project config**: Defaults in dbt_project.yml.


*Specific always overrides general.*

</back>