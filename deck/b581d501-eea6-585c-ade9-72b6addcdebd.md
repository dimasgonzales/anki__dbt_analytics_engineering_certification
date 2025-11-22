---
tags:
  - jinja-macros
  - modularity
citations:
- cleaned_docs/jinja-macros/index.md
guid: 97f31a5ddd
source: llm
uuid: b581d501-eea6-585c-ade9-72b6addcdebd
---

<front>

What is the syntax and file location required to define a custom macro in dbt?

</front>

---

<back>

Macros are defined using the `{% macro name(args) %}` block within `.sql` files located in the `macros/` directory.

Example:
```sql
-- macros/my_macro.sql
{% macro my_macro(arg) %}
  ...
{% endmacro %}
```

</back>
