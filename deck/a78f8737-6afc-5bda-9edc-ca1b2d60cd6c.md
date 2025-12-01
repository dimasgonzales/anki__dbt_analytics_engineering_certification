---
tags:
- card_type/factual
- deployment-jobs
- lineage
- modularity
citations:
- cleaned_docs/cli-commands/rank_4.md
guid: cb3ad01538
source: llm
uuid: a78f8737-6afc-5bda-9edc-ca1b2d60cd6c
---

<front>

How does the dbt Cloud CLI handle upstream dependencies by default when running a model locally?

</front>

---

<back>

It uses **Automatic Deferral**. The CLI automatically references the manifest from the project's production environment defined in dbt Cloud. This allows you to query upstream tables (like raw sources or staging models) without having to build them in your local schema first.

</back>
