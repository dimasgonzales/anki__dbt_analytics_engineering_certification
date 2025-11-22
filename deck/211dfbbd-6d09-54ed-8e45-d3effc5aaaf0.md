---
tags:
  - compiled-code
  - state-concepts
  - modularity
citations:
- cleaned_docs/jinja-macros/rank_6.md
guid: 84e6aeb217
source: llm
uuid: 211dfbbd-6d09-54ed-8e45-d3effc5aaaf0
---

<front>

You want to write a post-hook that performs a `VACUUM` operation on a table using `run_query`. Why might this command fail or behave unexpectedly regarding transactions?

</front>

---

<back>

`run_query` does not automatically begin a transaction. Furthermore, some commands like `VACUUM` cannot be executed inside a transaction block (depending on the warehouse). You must ensure the command is compatible with dbt's connection state or understand it executes as a side effect immediately.

</back>
