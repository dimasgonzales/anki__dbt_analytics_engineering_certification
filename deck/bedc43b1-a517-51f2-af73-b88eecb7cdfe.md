---
tags:
- card_type/factual
- debugging/compiled-code
- development/cli-commands
- state/state-concepts
citations:
- cleaned_docs/dbt-clone/rank_7.md
guid: 1c94d6ff00
source: llm
uuid: bedc43b1-a517-51f2-af73-b88eecb7cdfe
---

<front>

In the context of dbt operations, what does 'idempotency' mean?

</front>

---

<back>

Idempotency means that running a model once or multiple times on the same raw data produces the identical result. dbt does not track history internally between runs; it processes the current code and database state to reach the desired end state.

</back>
