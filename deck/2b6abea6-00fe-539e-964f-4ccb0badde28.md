---
tags:
- card_type/scenario
- cli-commands
- deployment-jobs
- lineage
citations:
- cleaned_docs/deployment-jobs/rank_2.md
guid: 9148741cb7
source: llm
uuid: 2b6abea6-00fe-539e-964f-4ccb0badde28
---

<front>

You are configuring a CI job to test a change to a downstream model. How do you ensure the job does not rebuild all unchanged upstream dependencies while still running successfully?

</front>

---

<back>

Enable 'Defer to a previous run' in the job settings and select the Production environment's manifest. This allows the job to use the production version of upstream models for `ref()` calls, building only the modified model and its children in the staging schema.

</back>
