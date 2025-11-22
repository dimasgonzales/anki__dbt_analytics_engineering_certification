---
tags:
  - versioning
  - dag-failures
citations:
- cleaned_docs/versioning/rank_2.md
guid: 313f701ec5
source: llm
uuid: 6b62da45-ad88-55aa-b3d6-fe17dbb9f7eb
---

<front>

Starting with dbt Core v1.8, how has the version dependency between `dbt-core` and adapter plugins (like `dbt-snowflake`) changed?

</front>

---

<back>

The versions are now **decoupled**. 

Prior to v1.8, adapter minor versions had to match the Core minor version exactly. From v1.8+ onwards, they coordinate via the `dbt-adapters` interface, allowing the adapter version to differ from the Core version.

</back>
