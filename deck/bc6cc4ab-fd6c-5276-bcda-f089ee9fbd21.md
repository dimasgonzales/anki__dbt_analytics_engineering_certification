---
tags:
- card_type/scenario
- error-logs
- packages
- seeds
citations:
- cleaned_docs/docs-generation/rank_7.md
guid: c4fa88cb36
source: llm
uuid: bc6cc4ab-fd6c-5276-bcda-f089ee9fbd21
---

<front>

You are joining `orders` (aliased as `o`) and `customers` (aliased as `c`). Both tables have a `created_at` column. How do you use `dbt_utils.star` to select all order columns without causing a compilation or runtime error?

</front>

---

<back>

You must pass the alias 'o' to the macro to ensure the columns are explicitly referenced:

```sql
select
  {{ dbt_utils.star(from=ref('orders'), relation_alias='o') }}
from {{ ref('orders') }} as o
...
```

</back>
