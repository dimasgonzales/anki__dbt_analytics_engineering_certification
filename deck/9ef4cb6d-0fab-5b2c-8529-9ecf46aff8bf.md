---
tags:
  - seeds
  - jinja-macros
  - cli-commands
citations:
- cleaned_docs/seeds/rank_3.md
guid: f2cb750930
source: llm
uuid: 9ef4cb6d-0fab-5b2c-8529-9ecf46aff8bf
---

<front>

You are loading a seed file containing Zip Codes (e.g., '02139'), but dbt is loading them as integers (2139), causing the loss of the leading zero. How do you resolve this?

</front>

---

<back>

Define the column as a string type using the `column_types` config. By explicitly setting the type to `varchar` (or your adapter's equivalent), dbt treats the data as text rather than inferring it as a number.

```yaml
seeds:
  my_project:
    zip_codes:
      +column_types:
        zip: varchar(5)
```

</back>
