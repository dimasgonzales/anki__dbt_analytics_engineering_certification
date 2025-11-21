Copy page

Model properties
================

Models properties can be declared in `.yml` files in your `models/` directory (as defined by the [`model-paths` config](/reference/project-configs/model-paths)).

You can name these files `whatever_you_want.yml`, and nest them arbitrarily deeply in subfolders within the `models/` directory.

models/<filename>.yml

```
models:  
  # Model name must match the filename of a model -- including case sensitivity  
  - name: model_name  
    description: <markdown_string>  
    latest_version: <version_identifier>  
    deprecation_date: <YAML_DateTime>  
    config:  
      <model_config>: <config_value>  
      docs:  
        show: true | false  
        node_color: <color_id> # Use name (such as node_color: purple) or hex code with quotes (such as node_color: "#cd7f32")  
      access: private | protected | public  
    constraints:  
      - <constraint>  
    data_tests:  
      - <test>  
      - ... # declare additional data tests  
    columns:  
      - name: <column_name> # required  
        description: <markdown_string>  
        quote: true | false  
        constraints:  
          - <constraint>  
        data_tests:  
          - <test>  
          - ... # declare additional data tests  
        config:  
          meta: {<dictionary>}  
          tags: [<string>]  
          
        # only required in conjunction with time_spine key  
        granularity: <any supported time granularity>   
  
      - name: ... # declare properties of additional columns  
  
    time_spine:  
      standard_granularity_column: <column_name>  
  
    versions:  
      - v: <version_identifier> # required  
        defined_in: <definition_file_name>  
        description: <markdown_string>  
        constraints:  
          - <constraint>  
        config:  
          <model_config>: <config_value>  
          docs:  
            show: true | false  
          access: private | protected | public  
        data_tests:  
          - <test>  
          - ... # declare additional data tests  
        columns:  
          # include/exclude columns from the top-level model properties  
          - include: <include_value>  
            exclude: <exclude_list>  
          # specify additional columns  
          - name: <column_name> # required  
            quote: true | false  
            constraints:  
              - <constraint>  
            data_tests:  
              - <test>  
              - ... # declare additional data tests  
            tags: [<string>]  
        - v: ... # declare additional versions
```