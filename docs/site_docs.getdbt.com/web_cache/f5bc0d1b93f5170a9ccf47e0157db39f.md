# Source: https://docs.getdbt.com/reference/data-test-configs

Data test configurations | dbt Developer Hub

[Skip to main content](#__docusaurus_skipToContent_fallback)

[✨ Live virtual event - Smarter pipelines, 29% more efficient: How the dbt Fusion engine optimizes data work on December 3rd!](https://www.getdbt.com/resources/webinars/how-the-dbt-fusion-engine-optimizes-data-work)

[![dbt Logo](/img/dbt-logo.svg?v=2)![dbt Logo](/img/dbt-logo-light.svg?v=2)](/)

[Docs](#)

* [Product docs](/docs/introduction)
* [References](/reference/references-overview)
* [Best practices](/best-practices)
* [Developer blog](/blog)

[Guides](/guides)[APIs](/docs/dbt-cloud-apis/overview)

[Help](#)

* [Release notes](/docs/dbt-versions/dbt-cloud-release-notes)
* [FAQs](/docs/faqs)
* [Support and billing](/docs/dbt-support)
* [Fusion Diaries](https://github.com/dbt-labs/dbt-fusion/discussions/categories/announcements)
* [Courses](https://learn.getdbt.com)

[Community](#)

* [Join the dbt Community](/community/join)
* [Become a contributor](/community/contribute)
* [Community forum](/community/forum)
* [Events](/community/events)
* [Spotlight](/community/spotlight)

[Account](#)

* [Log in to dbt](https://cloud.getdbt.com/)
* [Create a free account](https://www.getdbt.com/signup)

[Install VS Code extension](https://marketplace.visualstudio.com/items?itemName=dbtLabsInc.dbt)

[v](#) 

* dbt platform (Latest)
* dbt Fusion engine
* Core v1.11 Beta
* Core v1.10 (Compatible)
* Core v1.9 (Extended)

Search

[![dbt Logo](/img/dbt-logo.svg?v=2)![dbt Logo](/img/dbt-logo-light.svg?v=2)](/)

* [About References](/reference/references-overview)
* [Project configs](/category/project-configs)
* [Platform-specific configs](/reference/resource-configs/resource-configs)
* [Resource configs and properties](/reference/resource-configs/resource-path)

  + [About resource paths](/reference/resource-configs/resource-path)
  + [Configs and properties](/reference/configs-and-properties)
  + [General properties](/category/general-properties)
  + [General configs](/category/general-configs)
  + [For models](/reference/model-properties)
  + [For seeds](/reference/seed-properties)
  + [For snapshots](/reference/snapshot-properties)
  + [For data tests](/reference/data-test-configs)

    - [Data test configurations](/reference/data-test-configs)
    - [fail\_calc](/reference/resource-configs/fail_calc)
    - [limit](/reference/resource-configs/limit)
    - [severity, error\_if, and warn\_if](/reference/resource-configs/severity)
    - [store\_failures](/reference/resource-configs/store_failures)
    - [store\_failures\_as](/reference/resource-configs/store_failures_as)
    - [where](/reference/resource-configs/where)
  + [For unit tests](/reference/resource-properties/unit-tests)
  + [For sources](/reference/source-properties)
  + [For analyses](/reference/analysis-properties)
  + [For exposures](/reference/exposure-properties)
  + [For macros](/reference/macro-properties)
  + [For functions](/reference/function-properties)
* [Commands](/reference/dbt-commands)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Resource configs and properties](/reference/resource-configs/resource-path)
* For data tests

Copy page

On this page

Data test configurations
========================

Related documentation[​](#related-documentation "Direct link to Related documentation")
---------------------------------------------------------------------------------------

* [Data tests](/docs/build/data-tests)

Data tests can be configured in a few different ways:

1. Properties within `.yml` definition (generic tests only, see [test properties](/reference/resource-properties/data-tests) for full syntax)
2. A `config()` block within the test's SQL definition
3. In `dbt_project.yml`

Data test configs are applied hierarchically, in the order of specificity outlined above. In the case of a singular test, the `config()` block within the SQL definition takes precedence over configs in the project file. In the case of a specific instance of a generic test, the test's `.yml` properties would take precedence over any values set in its generic SQL definition's `config()`, which in turn would take precedence over values set in `dbt_project.yml`.

Available configurations[​](#available-configurations "Direct link to Available configurations")
------------------------------------------------------------------------------------------------

Click the link on each configuration option to read more about what it can do.

### Data test-specific configurations[​](#data-test-specific-configurations "Direct link to Data test-specific configurations")

Resource-specific configurations are applicable to only one dbt resource type rather than multiple resource types. You can define these settings in the project file (`dbt_project.yml`), a property file (`models/properties.yml` for models, similarly for other resources), or within the resource’s file using the `{{ config() }}` macro.

The following resource-specific configurations are only available to Data tests:

* Project file
* Config block
* Property file

dbt\_project.yml

```
data_tests:  
  <resource-path>:  
    +fail_calc: <string>  
    +limit: <integer>  
    +severity: error | warn  
    +error_if: <string>  
    +warn_if: <string>  
    +store_failures: true | false  
    +where: <string>
```

```
{{ config(  
    fail_calc = "<string>",  
    limit = <integer>,  
    severity = "error | warn",  
    error_if = "<string>",  
    warn_if = "<string>",  
    store_failures = true | false,  
    where = "<string>"  
) }}
```

```
<resource_type>:  
  - name: <resource_name>  
    data_tests:  
      - <test_name>: # # Actual name of the test. For example, dbt_utils.equality  
          name: # Human friendly name for the test. For example, equality_fct_test_coverage  
          description: "markdown formatting"  
          arguments: # available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.  
            <argument_name>: <argument_value>  
          config:  
            fail_calc: <string>  
            limit: <integer>  
            severity: error | warn  
            error_if: <string>  
            warn_if: <string>  
            store_failures: true | false  
            where: <string>  
  
    columns:  
      - name: <column_name>  
        data_tests:  
          - <test_name>:  
              name:   
              description: "markdown formatting"  
              arguments: # available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.  
                <argument_name>: <argument_value>  
              config:  
                fail_calc: <string>  
                limit: <integer>  
                severity: error | warn  
                error_if: <string>  
                warn_if: <string>  
                store_failures: true | false  
                where: <string>
```

This configuration mechanism is supported for specific instances of generic tests only. To configure a specific singular test, you should use the `config()` macro in its SQL definition.

### General configurations[​](#general-configurations "Direct link to General configurations")

General configurations provide broader operational settings applicable across multiple resource types. Like resource-specific configurations, these can also be set in the project file, property files, or within resource-specific files.

* Project file
* Config block
* Property file

dbt\_project.yml

```
data_tests:  
  <resource-path>:  
    +enabled: true | false  
    +tags: <string> | [<string>]  
    +meta: {dictionary}  
    # relevant for store_failures only  
    +database: <string>  
    +schema: <string>  
    +alias: <string>
```

```
{{ config(  
    enabled=true | false,  
    tags="<string>" | ["<string>"]  
    meta={dictionary},  
    database="<string>",  
    schema="<string>",  
    alias="<string>",  
) }}
```

```
<resource_type>:  
  - name: <resource_name>  
    data_tests:  
      - <test_name>: # Actual name of the test. For example, dbt_utils.equality  
          name: # Human friendly name for the test. For example, equality_fct_test_coverage  
          description: "markdown formatting"  
          arguments: # available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.  
            <argument_name>: <argument_value>  
          config:  
            enabled: true | false  
            tags: <string> | [<string>]  
            meta: {dictionary}  
            # relevant for store_failures only  
            database: <string>  
            schema: <string>  
            alias: <string>  
  
    columns:  
      - name: <column_name>  
        data_tests:  
          - <test_name>:  
              name:   
              description: "markdown formatting"  
              arguments: # available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.  
                <argument_name>: <argument_value>  
              config:  
                enabled: true | false  
                tags: <string> | [<string>]  
                meta: {dictionary}  
                # relevant for store_failures only  
                database: <string>  
                schema: <string>  
                alias: <string>
```

This configuration mechanism is supported for specific instances of generic data tests only. To configure a specific singular test, you should use the `config()` macro in its SQL definition.

### Examples[​](#examples "Direct link to Examples")

#### Add a tag to one test[​](#add-a-tag-to-one-test "Direct link to Add a tag to one test")

If a specific instance of a generic data test:

models/<filename>.yml

```
models:  
  - name: my_model  
    columns:  
      - name: id  
        data_tests:  
          - unique:  
              config:  
                tags: ['my_tag'] # changed to config in v1.10
```

If a singular data test:

tests/<filename>.sql

```
{{ config(tags = ['my_tag']) }}  
  
select ...
```

#### Set the default severity for all instances of a generic data test[​](#set-the-default-severity-for-all-instances-of-a-generic-data-test "Direct link to Set the default severity for all instances of a generic data test")

macros/<filename>.sql

```
{% test my_test() %}  
  
    {{ config(severity = 'warn') }}  
  
    select ...  
  
{% endtest %}
```

#### Disable all data tests from a package[​](#disable-all-data-tests-from-a-package "Direct link to Disable all data tests from a package")

dbt\_project.yml

```
data_tests:  
  package_name:  
    +enabled: false
```

#### Specify custom configurations for generic data tests[​](#specify-custom-configurations-for-generic-data-tests "Direct link to Specify custom configurations for generic data tests")

Beginning in dbt v1.9, you can use any custom config key to specify custom configurations for data tests. For example, the following specifies the `snowflake_warehouse` custom config that dbt should use when executing the `accepted_values` data test:

```
models:  
  - name: my_model  
    columns:  
      - name: color  
        data_tests:  
          - accepted_values:  
              arguments: # available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.  
                values: ['blue', 'red']  
              config:  
                severity: warn  
                snowflake_warehouse: my_warehouse
```

Given the config, the data test runs on a different Snowflake virtual warehouse than the one in your default connection to enable better price-performance with a different warehouse size or more granular cost allocation and visibility.

#### Add a description to generic and singular tests[​](#add-a-description-to-generic-and-singular-tests "Direct link to Add a description to generic and singular tests")

Starting from dbt v1.9 (also available to dbt [release tracks](/docs/dbt-versions/cloud-release-tracks)), you can add [descriptions](/reference/resource-properties/data-tests#description) to both generic and singular tests.

For a generic test, add the description in line with the existing YAML:

models/staging/<filename>.yml

```
models:  
  - name: my_model  
    columns:  
      - name: delivery_status  
        data_tests:  
          - accepted_values:  
              arguments: # available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.  
                values: ['delivered', 'pending', 'failed']  
              description: "This test checks whether there are unexpected delivery statuses. If it fails, check with logistics team"
```

You can also add descriptions to the Jinja macro that provides the core logic of a generic data test. Refer to the [Add description to generic data test logic](/best-practices/writing-custom-generic-tests#add-description-to-generic-data-test-logic) for more information.

For a singular test, define it in the test's directory:

tests/my\_custom\_test.yml

```
data_tests:   
  - name: my_custom_test  
    description: "This test checks whether the rolling average of returns is inside of expected bounds. If it isn't, flag to customer success team"
```

For more information refer to [Add a description to a data test](/reference/resource-properties/description#add-a-description-to-a-data-test).

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/data-test-configs.md)

Last updated on **Nov 19, 2025**

[Previous

updated\_at](/reference/resource-configs/updated_at)[Next

Data test configurations](/reference/data-test-configs)

* [Related documentation](#related-documentation)
* [Available configurations](#available-configurations)
  + [Data test-specific configurations](#data-test-specific-configurations)
  + [General configurations](#general-configurations)
  + [Examples](#examples)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/data-test-configs.md)

Get started

Start building with dbt.
------------------------

The free dbt VS Code extension is the best way to develop locally with the dbt Fusion Engine.

[Install free extension](https://marketplace.visualstudio.com/items?itemName=dbtLabsInc.dbt)
[Request your demo](https://www.getdbt.com/contact)

[![dbt Labs](/img/dbt-logo-light.svg?v=2)](/)

##### Resources

[VS Code Extension](/docs/about-dbt-extension)
[Resource Hub](https://www.getdbt.com/resources)
[dbt Learn](https://www.getdbt.com/dbt-learn)
[Certification](https://www.getdbt.com/dbt-certification)
[Developer Blog](/blog)

##### Community

[Join the Community](/community/join)
[Become a Contributor](/community/contribute)
[Open Source dbt Packages](https://hub.getdbt.com/)
[Community Forum](/community/forum)

##### Support

[Contact Support](/docs/dbt-support)
[Professional Services](https://www.getdbt.com/services)
[Find a Partner](https://www.getdbt.com/partner-directory)
[System Status](https://status.getdbt.com/)

##### Connect with Us

© 2025 dbt Labs, Inc. All Rights Reserved.

[Terms of Service](https://www.getdbt.com/terms-of-use/)
[Privacy Policy](https://www.getdbt.com/cloud/privacy-policy/)
[Security](https://www.getdbt.com/security/)
Cookie Settings