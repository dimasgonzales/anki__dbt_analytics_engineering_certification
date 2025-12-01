---
tags:
- card_type/factual
- compiled-code
- deployment-jobs
- sources
citations:
- cleaned_docs/selectors/rank_4.md
guid: 2e5e1cc5c9
source: llm
uuid: 60d9e3ad-b787-52f8-b4ef-74cdedaecd46
---

<front>

When enabling 'Run source freshness' via the dbt Cloud UI checkbox, where does it execute in the job sequence relative to other commands?

</front>

---

<back>

It executes **first**, before any manual commands defined in the job steps.

Note: If 'Generate docs on run' is also checked, that executes **last**.

</back>
