---
tags:
- compiled-code
- dag-failures
- test-types
citations:
- cleaned_docs/test-types/rank_1.md
guid: dc10605b22
source: llm
uuid: f3e7dd9f-ce7b-55ff-b556-1520e1dc7aea
---

<front>

You want to execute all generic tests in your project while skipping singular tests. What CLI command achieves this using direct selection?

</front>

---

<back>

You can directly select tests based on their type property:

```bash
dbt test --select "test_type:generic"
```
This targets the test nodes directly, ignoring singular tests defined in `.sql` files.

</back>
