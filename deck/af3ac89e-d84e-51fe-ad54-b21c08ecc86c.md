---
tags:
- card_type/scenario
- development/materializations
- development/snapshots
- documentation/exposures
citations:
- cleaned_docs/modularity/rank_1.md
guid: ba2647c918
source: llm
uuid: af3ac89e-d84e-51fe-ad54-b21c08ecc86c
---

<front>

You need to migrate a critical legacy SQL view used by the CEO to a dbt model. How do you ensure the migration doesn't break the dashboard during development?

</front>

---

<back>

Use the **Alongside Strategy**. Build the new dbt model alongside the existing view. Do not drop or alter the legacy view until the new dbt model has been fully audited and confirmed to produce identical results.

</back>
