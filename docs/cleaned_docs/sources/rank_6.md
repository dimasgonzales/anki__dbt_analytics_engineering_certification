Copy page

On this page

description
===========

models/schema.yml

```
models:  
  - name: model_name  
    description: markdown_string  
  
    columns:  
      - name: column_name  
        description: markdown_string
```

models/schema.yml

```
sources:  
  - name: source_name  
    description: markdown_string  
  
    tables:  
      - name: table_name  
        description: markdown_string  
  
        columns:  
          - name: column_name  
            description: markdown_string
```

seeds/schema.yml

```
seeds:  
  - name: seed_name  
    description: markdown_string  
  
    columns:  
      - name: column_name  
        description: markdown_string
```

snapshots/schema.yml

```
snapshots:  
  - name: snapshot_name  
    description: markdown_string  
  
    columns:  
      - name: column_name  
        description: markdown_string
```

analysis/schema.yml

```
analyses:  
  - name: analysis_name  
    description: markdown_string  
  
    columns:  
      - name: column_name  
        description: markdown_string
```

macros/schema.yml

```
macros:  
  - name: macro_name  
    description: markdown_string  
  
    arguments:  
      - name: argument_name  
        description: markdown_string
```

You can add a description to a [singular data test](/docs/build/data-tests#singular-data-tests) or a [generic data test](/docs/build/data-tests#generic-data-tests).

tests/schema.yml

```
# Singular data test example  
  
version: 2  
  
data_tests:  
  - name: data_test_name  
    description: markdown_string
```

tests/schema.yml

```
# Generic data test example  
  
version: 2  
  
models:  
  - name: model_name  
    columns:  
      - name: column_name  
        data_tests:  
          - unique:  
              description: markdown_string
```

models/schema.yml

```
unit_tests:  
  - name: unit_test_name  
    description: "markdown_string"  
    model: model_name   
    given: ts  
      - input: ref_or_source_call  
        rows:  
         - {column_name: column_value}  
         - {column_name: column_value}  
         - {column_name: column_value}  
         - {column_name: column_value}  
      - input: ref_or_source_call  
        format: csv  
        rows: dictionary | string  
    expect:   
      format: dict | csv | sql  
      fixture: fixture_name
```

Definition[​](#definition "Direct link to Definition")
------------------------------------------------------

A user-defined description used to document:

* a model, and model columns
* sources, source tables, and source columns
* seeds, and seed columns
* snapshots, and snapshot columns
* analyses, and analysis columns
* macros, and macro arguments
* data tests, and data test columns
* unit tests for models

These descriptions are used in the documentation website rendered by dbt (refer to [the documentation guide](/docs/build/documentation) or [Catalog](/docs/explore/explore-projects)).

Descriptions can include markdown, as well as the [`doc` Jinja function](/reference/dbt-jinja-functions/doc).

You may need to quote your YAML

Be mindful of YAML semantics when providing a description. If your description contains special YAML characters like curly brackets, colons, or square brackets, you may need to quote your description. An example of a quoted description is shown [below](#use-some-markdown-in-a-description).

Examples[​](#examples "Direct link to Examples")
------------------------------------------------

This section contains examples of how to add descriptions to various resources: