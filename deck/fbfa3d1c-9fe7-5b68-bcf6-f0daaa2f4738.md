---
tags:
- card_type/scenario
- development/modularity
- development/snapshots
- development/sources
citations:
- cleaned_docs/sources/rank_10.md
guid: eca3d1396f
source: llm
uuid: fbfa3d1c-9fe7-5b68-bcf6-f0daaa2f4738
---

<front>

A source contains 50 tables. 49 of them use `_etl_loaded_at` for freshness checks, but one table uses `last_modified`. How should you configure the YAML to be as DRY as possible?

</front>

---

<back>

Define the `loaded_at_field: _etl_loaded_at` at the top `source` level config to apply it as the default. Then, specifically for the one exception table, override the config with `loaded_at_field: last_modified`.

</back>
