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
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly supports the answer by stating that dbt operations are idempotent, meaning they produce the same transformed result given the same raw data, regardless of how many times they are run, and that dbt does not rely on prior runs but processes the current code and database state."
  citation:
    quote: "That is, it doesn't matter how many times a model has been run before, or if it has ever been run before. It doesn't matter if you run it once or a thousand times. Given the same raw data, you can expect the same transformed result. A given run of dbt doesn't need to 'know' about *any other* run; it just needs to know about the code in the project and the objects in your database as they exist *right now*."
    is_quote_valid: false
---

<front>

In the context of dbt operations, what does 'idempotency' mean?

</front>

---

<back>

Idempotency means that running a model once or multiple times on the same raw data produces the identical result. dbt does not track history internally between runs; it processes the current code and database state to reach the desired end state.

</back>
