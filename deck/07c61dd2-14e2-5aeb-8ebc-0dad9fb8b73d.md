---
tags:
- card_type/factual
- development/grants
- development/materializations
- governance/contracts
citations:
- cleaned_docs/grants/rank_2.md
guid: 5a5994a405
source: llm
uuid: 07c61dd2-14e2-5aeb-8ebc-0dad9fb8b73d
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly states that hooks are a method for granting schema-level permissions like 'GRANT USAGE ON SCHEMA', as the built-in 'grants' config does not handle schemas as objects."
  citation:
    quote: "Option A -- simple and familiar -- hooks to the rescue"
    is_quote_valid: true
---

<front>

What configuration method must be used to apply `GRANT USAGE ON SCHEMA` permissions in dbt?

</front>

---

<back>

You must use **Hooks** (specifically `on-run-end` or `post-hook`).

The `grants` resource config is scoped strictly to model objects (tables and views) and cannot handle schema-level permissions.

</back>
