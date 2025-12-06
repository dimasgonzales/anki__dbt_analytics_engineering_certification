# Source: https://docs.getdbt.com/reference/resource-configs/store_failures

store\_failures | dbt Developer Hub

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
* [For data tests](/reference/data-test-configs)
* store\_failures

Copy page

On this page

store\_failures
===============

The configured test(s) will store their failures when `dbt test --store-failures` is invoked. If you set this configuration as `false` but [`store_failures_as`](/reference/resource-configs/store_failures_as) is configured, it will be overridden.

Description[​](#description "Direct link to Description")
---------------------------------------------------------

Optionally set a test to always or never store its failures in the database.

* If specified as `true` or `false`, the
  `store_failures` config will take precedence over the presence or absence of the `--store-failures` flag.
* If the `store_failures` config is `none` or omitted, the resource will use the value of the `--store-failures` flag.
* When true, `store_failures` saves all records (up to [limit](/reference/resource-configs/limit)) that failed the test. Failures are saved in a new table with the name of the test.
* A test's results will always **replace** previous failures for the same test, even if that test results in no failures.
* By default, `store_failures` uses a schema named `{{ profile.schema }}_dbt_test__audit`, but, you can [configure](/reference/resource-configs/schema#tests) the schema to a different value. Ensure you have the authorization to create or access schemas for your work. For more details, refer to the [FAQ](#faqs).

This logic is encoded in the [`should_store_failures()`](https://github.com/dbt-labs/dbt-adapters/blob/60005a0a2bd33b61cb65a591bc1604b1b3fd25d5/dbt/include/global_project/macros/materializations/configs.sql#L15) macro.

* Specific test
* Singular test
* Generic test block
* Project level

Configure a specific instance of a generic (schema) test:

models/<filename>.yml

```
models:  
  - name: my_model  
    columns:  
      - name: my_column  
        data_tests:  
          - unique:  
              config:  
                store_failures: true  # always store failures  
          - not_null:  
              config:  
                store_failures: false  # never store failures
```

Configure a singular (data) test:

tests/<filename>.sql

```
{{ config(store_failures = true) }}  
  
select ...
```

Set the default for all instances of a generic (schema) test, by setting the config inside its test block (definition):

macros/<filename>.sql

```
{% test <testname>(model, column_name) %}  
  
{{ config(store_failures = false) }}  
  
select ...  
  
{% endtest %}
```

Set the default for all tests in a package or project:

dbt\_project.yml

```
data_tests:  
  +store_failures: true  # all tests  
    
  <package_name>:  
    +store_failures: false # tests in <package_name>
```

FAQs[​](#faqs "Direct link to FAQs")
------------------------------------

Receiving a 'permissions denied for schema' error

If you're receiving a `Adapter name adapter: Adapter_name error: permission denied for schema dev_username_dbt_test__audit`, this is most likely due to your user not having permission to create new schemas, despite having owner access to your own development schema.

To resolve this, you need proper authorization to create or access custom schemas. Run the following SQL command in your respective data platform environment. Note that the exact authorization query may differ from one data platform to another:

```
create schema if not exists dev_username_dbt_test__audit authorization username;
```

*Replace `dev_username` with your specific development schema name and `username` with the appropriate user who should have the permissions.*

This command grants the appropriate permissions to create and access the `dbt_test__audit` schema, which is often used with the `store_failures` configuration.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/store_failures.md)

Last updated on **Nov 19, 2025**

[Previous

severity, error\_if, and warn\_if](/reference/resource-configs/severity)[Next

store\_failures\_as](/reference/resource-configs/store_failures_as)

* [Description](#description)
* [FAQs](#faqs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/store_failures.md)

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