---
tags:
- card_type/scenario
- development/cli-commands
- development/seeds
- documentation/exposures
citations:
- cleaned_docs/exposures/rank_1.md
guid: 88154c03d4
source: llm
uuid: e5aa8d7a-d6d5-54ca-82eb-9bcbde647fa7
---

<front>

You want to execute a `dbt run` command that builds all models feeding into your 'weekly_dashboard' exposure. How would you accomplish this?

</front>

---

<back>

Use the `+` prefix selector combined with the `exposure:` selection syntax.

Command:
```bash
dbt run --select +exposure:weekly_dashboard
```
This selects the exposure and all of its upstream parents defined in the `depends_on` list.

</back>
