---
tags:
- card_type/scenario
- debugging/error-logs
- development/materializations
- pipelines/deployment-jobs
citations:
- cleaned_docs/jinja-macros/rank_7.md
guid: 0a2d4cb3f6
source: llm
uuid: 19df4c28-96ae-5ee8-babc-b49fc7eb0ef9
---

<front>

You are reviewing a Pull Request for a production deployment and see the following line inside a complex macro: `{{ debug() }}`. What action should you take?

</front>

---

<back>

Request changes to remove the line. This code must not be merged because it will break automated jobs by pausing execution to wait for user input that will never come.

</back>
