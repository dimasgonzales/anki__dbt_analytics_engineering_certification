# Source: https://docs.getdbt.com/docs/build/data-tests

Add data tests to your DAG | dbt Developer Hub

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

* About
* [What is dbt?](/docs/introduction)
* [dbt Fusion engine](/docs/fusion)
* [About the dbt platform](/docs/cloud/about-cloud/dbt-cloud-features)
* [Supported data platforms](/docs/supported-data-platforms)
* Get started
* [Get started with dbt](/docs/get-started-dbt)
* [Set up dbt](/docs/about-setup)
* Build and develop
* [Develop with dbt](/docs/cloud/about-develop-dbt)
* [Build dbt projects](/docs/build/projects)

  + [About dbt projects](/docs/build/projects)
  + [dbt tips and tricks](/docs/build/dbt-tips)
  + [Build your DAG](/docs/build/models)

    - [Models](/docs/build/models)
    - [Tests](/docs/build/data-tests)

      * [Data tests](/docs/build/data-tests)
      * [Unit tests](/docs/build/unit-tests)
    - [Documentation](/docs/build/documentation)
    - [Snapshots](/docs/build/snapshots)
    - [Seeds](/docs/build/seeds)
    - [Jinja and macros](/docs/build/jinja-macros)
    - [User-defined functions](/docs/build/udfs)
    - [Sources](/docs/build/sources)
    - [Exposures](/docs/build/exposures)
    - [Groups](/docs/build/groups)
    - [Analyses](/docs/build/analyses)
  + [Build your metrics](/docs/build/build-metrics-intro)
  + [Enhance your models](/docs/build/enhance-your-models)
  + [Enhance your code](/docs/build/enhance-your-code)
  + [Organize your outputs](/docs/build/organize-your-outputs)
  + [Optimize development](/docs/build/empty-flag)
* [Build dbt Mesh](/docs/mesh/about-mesh)
* Deploy and explore
* [Deploy dbt](/docs/deploy/deployments)
* [Explore your data](/docs/explore/explore-your-data)
* [Use the dbt Semantic Layer](/docs/use-dbt-semantic-layer/dbt-sl)
* dbt AI
* [Copilot](/docs/cloud/dbt-copilot)
* [dbt MCP](/docs/dbt-ai/about-mcp)
* Additional tools
* [dbt integrations](/docs/cloud-integrations/overview)
* [Cost management](/docs/cloud/cost-management)
* Release information
* [Available dbt versions](/docs/dbt-versions/about-versions)
* [dbt release notes](/docs/dbt-versions/dbt-cloud-release-notes)

* [Build dbt projects](/docs/build/projects)
* [Build your DAG](/docs/build/models)
* Tests

Copy page

On this page

Add data tests to your DAG
==========================

Tip

Use [dbt Copilot](/docs/cloud/dbt-copilot), available for dbt Enterprise and Enterprise+ accounts, to generate data tests in the Studio IDE only.

Related reference docs[​](#related-reference-docs "Direct link to Related reference docs")
------------------------------------------------------------------------------------------

* [Test command](/reference/commands/test)
* [Data test properties](/reference/resource-properties/data-tests)
* [Data test configurations](/reference/data-test-configs)
* [Test selection examples](/reference/node-selection/test-selection-examples)

important

Tests are now called data tests to disambiguate from [unit tests](/docs/build/unit-tests). The YAML key `tests:` is still supported as an alias for `data_tests:`. Refer to [New `data_tests:` syntax](#new-data_tests-syntax) for more information.

Overview[​](#overview "Direct link to Overview")
------------------------------------------------

Data tests are assertions you make about your models and other resources in your dbt project (for example, sources, seeds, and snapshots). When you run `dbt test`, dbt will tell you if each test in your project passes or fails.

You can use data tests to improve the integrity of the SQL in each model by making assertions about the results generated. Out of the box, you can test whether a specified column in a model only contains non-null values, unique values, or values that have a corresponding value in another model (for example, a `customer_id` for an `order` corresponds to an `id` in the `customers` model), and values from a specified list. You can extend data tests to suit business logic specific to your organization – any assertion that you can make about your model in the form of a select query can be turned into a data test.

Data tests return a set of failing records. Generic data tests (a.k.a. schema tests) are defined using `test` blocks.

Like almost everything in dbt, data tests are SQL queries. In particular, they are `select` statements that seek to grab "failing" records, ones that disprove your assertion. If you assert that a column is unique in a model, the test query selects for duplicates; if you assert that a column is never null, the test seeks after nulls. If the data test returns zero failing rows, it passes, and your assertion has been validated.

There are two ways of defining data tests in dbt:

* A **singular** data test is testing in its simplest form: If you can write a SQL query that returns failing rows, you can save that query in a `.sql` file within your [test directory](/reference/project-configs/test-paths). It's now a data test, and it will be executed by the `dbt test` command.
* A **generic** data test is a parameterized query that accepts arguments. The test query is defined in a special `test` block (like a [macro](/docs/build/jinja-macros)). Once defined, you can reference the generic test by name throughout your `.yml` files—define it on models, columns, sources, snapshots, and seeds. dbt ships with four generic data tests built in, and we think you should use them!

Defining data tests is a great way to confirm that your outputs and inputs are as expected, and helps prevent regressions when your code changes. Because you can use them over and over again, making similar assertions with minor variations, generic data tests tend to be much more common—they should make up the bulk of your dbt data testing suite. That said, both ways of defining data tests have their time and place.

Creating your first data tests

If you're new to dbt, we recommend that you check out our [online dbt Fundamentals course](https://learn.getdbt.com/learn/course/dbt-fundamentals/data-tests-30min/building-tests?page=1) or [quickstart guide](/guides) to build your first dbt project with models and tests.

Singular data tests[​](#singular-data-tests "Direct link to Singular data tests")
---------------------------------------------------------------------------------

The simplest way to define a data test is by writing the exact SQL that will return failing records. We call these "singular" data tests, because they're one-off assertions usable for a single purpose.

These tests are defined in `.sql` files, typically in your `tests` directory (as defined by your [`test-paths` config](/reference/project-configs/test-paths)). You can use Jinja (including `ref` and `source`) in the test definition, just like you can when creating models. Each `.sql` file contains one `select` statement, and it defines one data test:

tests/assert\_total\_payment\_amount\_is\_positive.sql

```
-- Refunds have a negative amount, so the total amount should always be >= 0.  
-- Therefore return records where total_amount < 0 to make the test fail.  
select  
    order_id,  
    sum(amount) as total_amount  
from {{ ref('fct_payments') }}  
group by 1  
having total_amount < 0
```

The name of this test is the name of the file: `assert_total_payment_amount_is_positive`.

Note:

* Omit semicolons (;) at the end of the SQL statement in your singular test files, as they can cause your data test to fail.
* Singular data tests placed in the tests directory are automatically executed when running `dbt test`. Don't reference singular tests in `model_name.yml`, as they are not treated as generic tests or macros, and doing so will result in an error.

To add a description to a singular data test in your project, add a `.yml` file to your `tests` directory, for example, `tests/schema.yml` with the following content:

tests/schema.yml

```
data_tests:  
  - name: assert_total_payment_amount_is_positive  
    description: >  
      Refunds have a negative amount, so the total amount should always be >= 0.  
      Therefore return records where total amount < 0 to make the test fail.
```

Singular data tests are so easy that you may find yourself writing the same basic structure repeatedly, only changing the name of a column or model. By that point, the test isn't so singular! In that case, we recommend generic data tests.

Generic data tests[​](#generic-data-tests "Direct link to Generic data tests")
------------------------------------------------------------------------------

Certain data tests are generic: they can be reused over and over again. A generic data test is defined in a `test` block, which contains a parametrized query and accepts arguments. It might look like:

```
{% test not_null(model, column_name) %}  
  
    select *  
    from {{ model }}  
    where {{ column_name }} is null  
  
{% endtest %}
```

You'll notice that there are two arguments, `model` and `column_name`, which are then templated into the query. This is what makes the data test "generic": it can be defined on as many columns as you like, across as many models as you like, and dbt will pass the values of `model` and `column_name` accordingly. Once that generic test has been defined, it can be added as a *property* on any existing model (or source, seed, or snapshot). These properties are added in `.yml` files in the same directory as your resource.

info

If this is your first time working with adding properties to a resource, check out the docs on [declaring properties](/reference/configs-and-properties).

Out of the box, dbt ships with four generic data tests already defined: `unique`, `not_null`, `accepted_values` and `relationships`. Here's a full example using those tests on an `orders` model:

```
models:  
  - name: orders  
    columns:  
      - name: order_id  
        data_tests:  
          - unique  
          - not_null  
      - name: status  
        data_tests:  
          - accepted_values:  
              arguments: # available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.  
                values: ['placed', 'shipped', 'completed', 'returned']  
      - name: customer_id  
        data_tests:  
          - relationships:  
              arguments:  
                to: ref('customers')  
                field: id
```

In plain English, these data tests translate to:

* `unique`: the `order_id` column in the `orders` model should be unique
* `not_null`: the `order_id` column in the `orders` model should not contain null values
* `accepted_values`: the `status` column in the `orders` should be one of `'placed'`, `'shipped'`, `'completed'`, or `'returned'`
* `relationships`: each `customer_id` in the `orders` model exists as an `id` in the `customers` table (also known as referential integrity)

Behind the scenes, dbt constructs a `select` query for each data test, using the parametrized query from the generic test block. These queries return the rows where your assertion is *not* true; if the test returns zero rows, your assertion passes.

You can find more information about these data tests, and additional configurations (including [`severity`](/reference/resource-configs/severity) and [`tags`](/reference/resource-configs/tags)) in the [reference section](/reference/resource-properties/data-tests). You can also add descriptions to the Jinja macro that provides the core logic of a generic data test. Refer to the [Add description to generic data test logic](/best-practices/writing-custom-generic-tests#add-description-to-generic-data-test-logic) for more information.

### More generic data tests[​](#more-generic-data-tests "Direct link to More generic data tests")

Those four tests are enough to get you started. You'll quickly find you want to use a wider variety of data tests — a good thing! You can also install generic data tests from a package, or write your own, to use (and reuse) across your dbt project. Check out the [guide on custom generic data tests](/best-practices/writing-custom-generic-tests) for more information.

info

There are generic data tests defined in some open-source packages, such as [dbt-utils](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/) and [dbt-expectations](https://hub.getdbt.com/calogica/dbt_expectations/latest/) — skip ahead to the docs on [packages](/docs/build/packages) to learn more!

### Example[​](#example "Direct link to Example")

To add a generic (or "schema") data test to your project:

1. Add a `.yml` file to your `models` directory, for example, `models/schema.yml`, with the following content (you may need to adjust the `name:` values for an existing model)

models/schema.yml

```
models:  
  - name: orders  
    columns:  
      - name: order_id  
        data_tests:  
          - unique  
          - not_null
```

2. Run the [`dbt test` command](/reference/commands/test):

```
$ dbt test  
  
Found 3 models, 2 tests, 0 snapshots, 0 analyses, 130 macros, 0 operations, 0 seed files, 0 sources  
  
17:31:05 | Concurrency: 1 threads (target='learn')  
17:31:05 |  
17:31:05 | 1 of 2 START test not_null_order_order_id..................... [RUN]  
17:31:06 | 1 of 2 PASS not_null_order_order_id........................... [PASS in 0.99s]  
17:31:06 | 2 of 2 START test unique_order_order_id....................... [RUN]  
17:31:07 | 2 of 2 PASS unique_order_order_id............................. [PASS in 0.79s]  
17:31:07 |  
17:31:07 | Finished running 2 tests in 7.17s.  
  
Completed successfully  
  
Done. PASS=2 WARN=0 ERROR=0 SKIP=0 TOTAL=2
```

3. Check out the SQL dbt is running by either:
   * **dbt:** checking the Details tab.
   * **dbt Core:** checking the `target/compiled` directory

**Unique test**

* Compiled SQL
* Templated SQL

```
select *  
from (  
  
    select  
        order_id  
  
    from analytics.orders  
    where order_id is not null  
    group by order_id  
    having count(*) > 1  
  
) validation_errors
```

```
select *  
from (  
  
    select  
        {{ column_name }}  
  
    from {{ model }}  
    where {{ column_name }} is not null  
    group by {{ column_name }}  
    having count(*) > 1  
  
) validation_errors
```

**Not null test**

* Compiled SQL
* Templated SQL

```
select *  
from analytics.orders  
where order_id is null
```

```
select *  
from {{ model }}  
where {{ column_name }} is null
```

Storing data test failures[​](#storing-data-test-failures "Direct link to Storing data test failures")
------------------------------------------------------------------------------------------------------

Normally, a data test query will calculate failures as part of its execution. If you set the optional `--store-failures` flag, the [`store_failures`](/reference/resource-configs/store_failures), or the [`store_failures_as`](/reference/resource-configs/store_failures_as) configs, dbt will first save the results of a test query to a table in the database, and then query that table to calculate the number of failures.

This workflow allows you to query and examine failing records much more quickly in development:

[![Store test failures in the database for faster development-time debugging.](/img/docs/building-a-dbt-project/test-store-failures.gif?v=2 "Store test failures in the database for faster development-time debugging.")](#)Store test failures in the database for faster development-time debugging.

Note that, if you select to store data test failures:

* Test result tables are created in a schema suffixed or named `dbt_test__audit`, by default. It is possible to change this value by setting a `schema` config. (For more details on schema naming, see [using custom schemas](/docs/build/custom-schemas).)

* A test's results will always **replace** previous failures for the same test.

New `data_tests:` syntax[​](#new-data_tests-syntax "Direct link to new-data_tests-syntax")
------------------------------------------------------------------------------------------

Data tests were historically called "tests" in dbt as the only form of testing available. With the introduction of unit tests, the key was renamed from `tests:` to `data_tests:`.

dbt still supports `tests:` in your YML configuration files for backwards-compatibility purposes, and you might see it used throughout our documentation. However, you can't have a `tests` and a `data_tests` key associated with the same resource (for example, a single model) at the same time.

models/schema.yml

```
models:  
  - name: orders  
    columns:  
      - name: order_id  
        data_tests:  
          - unique  
          - not_null
```

dbt\_project.yml

```
data_tests:  
  +store_failures: true
```

FAQs[​](#faqs "Direct link to FAQs")
------------------------------------

What data tests are available for me to use in dbt?

Out of the box, dbt ships with the following data tests:

* `unique`
* `not_null`
* `accepted_values`
* `relationships` (i.e. referential integrity)

You can also write your own [custom schema data tests](/docs/build/data-tests).

Some additional custom schema tests have been open-sourced in the [dbt-utils package](https://github.com/dbt-labs/dbt-utils?#generic-tests), check out the docs on [packages](/docs/build/packages) to learn how to make these tests available in your project.

Note that although you can't document data tests as of yet, we recommend checking out [this dbt Core discussion](https://github.com/dbt-labs/dbt-core/issues/2578) where the dbt community shares ideas.

How do I test one model at a time?

Running tests on one model looks very similar to running a model: use the `--select` flag (or `-s` flag), followed by the name of the model:

```
dbt test --select customers
```

Check out the [model selection syntax documentation](/reference/node-selection/syntax) for full syntax, and [test selection examples](/reference/node-selection/test-selection-examples) in particular.

One of my tests failed, how can I debug it?

To debug a failing test, find the SQL that dbt ran by:

* dbt:

  + Within the test output, click on the failed test, and then select "Details".
* dbt Core:

  + Open the file path returned as part of the error message.
  + Navigate to the `target/compiled/schema_tests` directory for all compiled test queries.

Copy the SQL into a query editor (in dbt, you can paste it into a new `Statement`), and run the query to find the records that failed.

What data tests should I add to my project?

We recommend that every model has a data test on a primary key, that is, a column that is `unique` and `not_null`.

We also recommend that you test any assumptions on your source data. For example, if you believe that your payments can only be one of three payment methods, you should test that assumption regularly — a new payment method may introduce logic errors in your SQL.

In advanced dbt projects, we recommend using [sources](/docs/build/sources) and running these source data-integrity tests against the sources rather than models.

When should I run my data tests?

You should run your data tests whenever you are writing new code (to ensure you haven't broken any existing models by changing SQL), and whenever you run your transformations in production (to ensure that your assumptions about your source data are still valid).

Can I store my data tests in a directory other than the `tests` directory in my project?

By default, dbt expects your singular data test files to be located in the `tests` subdirectory of your project, and generic data test definitions to be located in `tests/generic` or `macros`.

To change this, update the [test-paths](/reference/project-configs/test-paths) configuration in your `dbt_project.yml`
file, like so:

dbt\_project.yml

```
test-paths: ["my_cool_tests"]
```

Then, you can define generic data tests in `my_cool_tests/generic/`, and singular data tests everywhere else in `my_cool_tests/`.

How do I run data tests on just my sources?

To run data tests on all sources, use the following command:

```
  dbt test --select "source:*"
```

(You can also use the `-s` shorthand here instead of `--select`)

To run data tests on one source (and all of its tables):

```
$ dbt test --select source:jaffle_shop
```

And, to run data tests on one source table only:

```
$ dbt test --select source:jaffle_shop.orders
```

Can I set test failure thresholds?

You can use the `error_if` and `warn_if` configs to set custom failure thresholds in your tests. For more details, see [reference](/reference/resource-configs/severity) for more information.

You can also try the following solutions:

* Setting the [severity](/reference/resource-configs/severity) to `warn` or `error`
* Writing a [custom generic test](/best-practices/writing-custom-generic-tests) that accepts a threshold argument ([example](https://discourse.getdbt.com/t/creating-an-error-threshold-for-schema-tests/966))

Can I test the uniqueness of two columns?

Yes, there's a few different options.

Consider an orders table that contains records from multiple countries, and the combination of ID and country code is unique:

| order\_id | country\_code |
| --- | --- |
| 1 | AU |
| 2 | AU |
| ... | ... |
| 1 | US |
| 2 | US |
| ... | ... |

Here are some approaches:

#### 1. Create a unique key in the model and test that[​](#1-create-a-unique-key-in-the-model-and-test-that "Direct link to 1. Create a unique key in the model and test that")

models/orders.sql

```
select  
  country_code || '-' || order_id as surrogate_key,  
  ...
```

models/orders.yml

```
version: 2  
  
models:  
  - name: orders  
    columns:  
      - name: surrogate_key  
        data_tests:  
          - unique
```

#### 2. Test an expression[​](#2-test-an-expression "Direct link to 2. Test an expression")

models/orders.yml

```
version: 2  
  
models:  
  - name: orders  
    data_tests:  
      - unique:  
          arguments: # available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.  
            column_name: "(country_code || '-' || order_id)"
```

#### 3. Use the `dbt_utils.unique_combination_of_columns` test[​](#3-use-the-dbt_utilsunique_combination_of_columns-test "Direct link to 3-use-the-dbt_utilsunique_combination_of_columns-test")

This is especially useful for large datasets since it is more performant. Check out the docs on [packages](/docs/build/packages) for more information.

models/orders.yml

```
version: 2  
  
models:  
  - name: orders  
    data_tests:  
      - dbt_utils.unique_combination_of_columns:  
          arguments: # available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.  
            combination_of_columns:  
              - country_code  
              - order_id
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

100

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/data-tests.md)

Last updated on **Nov 19, 2025**

[Next

Unit tests](/docs/build/unit-tests)

* [Related reference docs](#related-reference-docs)
* [Overview](#overview)
* [Singular data tests](#singular-data-tests)
* [Generic data tests](#generic-data-tests)
  + [More generic data tests](#more-generic-data-tests)
  + [Example](#example)
* [Storing data test failures](#storing-data-test-failures)
* [New `data_tests:` syntax](#new-data_tests-syntax)
* [FAQs](#faqs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/data-tests.md)

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




![dbt Labs](https://cdn.cookielaw.org/logos/4a2cde9e-5f84-44b2-bdbb-6a93354d1c72/e1199e19-1935-49fa-a4e2-bf7f9d08cee6/783d7c83-af8c-4032-901b-b3ec48982078/dbt-logo.png)

Privacy Preference Center
-------------------------

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer.
  
[More information](https://www.getdbt.com/cloud/privacy-policy/)

Allow All

### Manage Consent Preferences

#### Strictly Necessary Cookies

Always Active

Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.

#### Performance Cookies

Always Active

Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.

#### Targeting Cookies

Always Active

Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.

#### Functional Cookies

Always Active

Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox label label

Apply Cancel

Consent Leg.Interest

checkbox label label

checkbox label label

checkbox label label

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg "Powered by OneTrust Opens in a new Tab")](https://www.onetrust.com/products/cookie-consent/)