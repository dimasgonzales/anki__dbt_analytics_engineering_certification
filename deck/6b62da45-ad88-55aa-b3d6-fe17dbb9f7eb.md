---
tags:
- card_type/factual
- governance/versioning
- pipelines/dag-failures
citations:
- cleaned_docs/versioning/rank_2.md
guid: 313f701ec5
source: llm
uuid: 6b62da45-ad88-55aa-b3d6-fe17dbb9f7eb
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly confirms that from dbt Core v1.8 onwards, adapter minor and patch versions can differ from Core versions, coordinated via the `dbt-adapters` interface, and prior to v1.8, versions had to match, supporting the answer's claim of decoupling."
  citation:
    quote: "Unlike `dbt-core` versions before 1.8, the minor and patch version numbers might not match between `dbt-core` and the adapter plugin(s) you've installed. For example, you might find you're using `dbt-core==1.8.0` with `dbt-snowflake==1.9.0`. Even though these don't have the same minor version, they can still work together as they both work with `dbt-adapters==1.8.0`."
    is_quote_valid: true
---

<front>

Starting with dbt Core v1.8, how has the version dependency between `dbt-core` and adapter plugins (like `dbt-snowflake`) changed?

</front>

---

<back>

The versions are now **decoupled**. 

Prior to v1.8, adapter minor versions had to match the Core minor version exactly. From v1.8+ onwards, they coordinate via the `dbt-adapters` interface, allowing the adapter version to differ from the Core version.

</back>
