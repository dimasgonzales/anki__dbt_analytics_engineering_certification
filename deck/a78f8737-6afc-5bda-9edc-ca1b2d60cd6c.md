---
tags:
- card_type/factual
- development/modularity
- documentation/lineage
- pipelines/deployment-jobs
citations:
- cleaned_docs/cli-commands/rank_4.md
guid: cb3ad01538
source: llm
uuid: a78f8737-6afc-5bda-9edc-ca1b2d60cd6c
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly confirms the use of automatic deferral to the production environment in the dbt Cloud CLI, which aligns with the answer's core claim about handling upstream dependencies locally without building them."
  citation:
    evidence_source: "https://docs.getdbt.com/docs/cloud/configure-cloud-cli"
    quote: "Automatic deferral of build artifacts to your Cloud project's production environment."
    is_quote_valid: true
---

<front>

How does the dbt Cloud CLI handle upstream dependencies by default when running a model locally?

</front>

---

<back>

It uses **Automatic Deferral**. The CLI automatically references the manifest from the project's production environment defined in dbt Cloud. This allows you to query upstream tables (like raw sources or staging models) without having to build them in your local schema first.

</back>
