---
tags:
- cli-commands
- compiled-code
- selectors
citations:
- cleaned_docs/test-types/rank_1.md
guid: 9d982183f4
source: llm
uuid: bd5a1b3b-5aee-5df4-9e05-deffe5ab913d
---

<front>

You have a model `orders` tagged `finance`. It has a unique test on `order_id` (not explicitly tagged). If you run `dbt test --select tag:finance`, the test runs. Is this Direct or Indirect selection?

</front>

---

<back>

This is **Indirect Selection**. 

The test itself did not inherit the `finance` tag. The command selected the `orders` model (the parent), which implicitly triggered the attached test.

</back>
