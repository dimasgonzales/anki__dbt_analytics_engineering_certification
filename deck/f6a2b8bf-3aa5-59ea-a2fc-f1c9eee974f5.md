---
tags:
- card_type/scenario
- development/modularity
- development/seeds
- documentation/exposures
citations:
- cleaned_docs/exposures/rank_9.md
guid: f21c501bd5
source: llm
uuid: f6a2b8bf-3aa5-59ea-a2fc-f1c9eee974f5
---

<front>

Stakeholders complain that their CEO Dashboard is stale even though the dbt job finished 30 minutes ago. What orchestration step is likely missing?

</front>

---

<back>

The orchestration pipeline likely lacks a **trigger** for the dashboard refresh. To solve this, define the dashboard as an **exposure** and configure the deployment job to trigger the BI tool's refresh API immediately upon the successful completion of `dbt build`, eliminating the latency gap.

</back>
