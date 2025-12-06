---
tags:
- card_type/factual
- development/jinja-macros
- development/modularity
- development/project-config
citations:
- cleaned_docs/jinja-macros/index.md
guid: 97f31a5ddd
source: llm
uuid: b581d501-eea6-585c-ade9-72b6addcdebd
claim_meta:
  verdict: NOT_FOUND
  explanation: "The reference text provides evidence supporting the syntax for defining macros, as shown in the macro example, but it does not contain any information about the file location or file type (.sql files in the macros/ directory) required to define custom macros."
  citation:
    quote: "{% macro generate_schema_name(custom_schema_name, node) -%} ... {%- endmacro %}"
    is_quote_valid: false
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
