# Source: https://docs.getdbt.com/best-practices/writing-custom-generic-tests

Writing custom generic data tests | dbt Developer Hub

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

* [Best practices](/best-practices)

  + [How we structure our dbt projects](/best-practices/how-we-structure/1-guide-overview)
  + [How we style our dbt projects](/best-practices/how-we-style/0-how-we-style-our-dbt-projects)
  + [How we build our metrics](/best-practices/how-we-build-our-metrics/semantic-layer-1-intro)
  + [How we build our dbt Mesh projects](/best-practices/how-we-mesh/mesh-1-intro)
  + [Materialization best practices](/best-practices/materializations/1-guide-overview)
  + [Don't nest your curlies](/best-practices/dont-nest-your-curlies)
  + [Clone incremental models as the first step of your CI job](/best-practices/clone-incremental-models)
  + [Writing custom generic data tests](/best-practices/writing-custom-generic-tests)
  + [Best practices for workflows](/best-practices/best-practice-workflows)
  + [Best practices for dbt and Unity Catalog](/best-practices/dbt-unity-catalog-best-practices)

* [Best practices](/best-practices)
* Writing custom generic data tests

Copy page

On this page

Writing custom generic data tests
=================================

dbt ships with [Not Null](/reference/resource-properties/data-tests#not-null), [Unique](/reference/resource-properties/data-tests#unique), [Relationships](/reference/resource-properties/data-tests#relationships), and [Accepted Values](/reference/resource-properties/data-tests#accepted-values) generic data tests. (These used to be called "schema tests," and you'll still see that name in some places.) Under the hood, these generic data tests are defined as `test` blocks (like macros).

info

There are tons of generic data tests defined in open source packages, such as [dbt-utils](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/) and [dbt-expectations](https://hub.getdbt.com/calogica/dbt_expectations/latest/) — the test you're looking for might already be here!

### Generic tests with standard arguments[​](#generic-tests-with-standard-arguments "Direct link to Generic tests with standard arguments")

Generic tests are defined in SQL files. Those files can live in two places:

* `tests/generic/`: that is, a special subfolder named `generic` within your [test paths](/reference/project-configs/test-paths) (`tests/` by default)
* `macros/`: Why? Generic tests work a lot like macros, and historically, this was the only place they could be defined. If your generic test depends on complex macro logic, you may find it more convenient to define the macros and the generic test in the same file.

To define your own generic tests, simply create a `test` block called `<test_name>`. All generic tests should accept one or both of the standard arguments:

* `model`: The resource on which the test is defined, templated out to its relation name. (Note that the argument is always named `model`, even when the resource is a source, seed, or snapshot.)
* `column_name`: The column on which the test is defined. Not all generic tests operate on the column level, but if they do, they should accept `column_name` as an argument.

Here's an example of an `is_even` schema test that uses both arguments:

tests/generic/test\_is\_even.sql

```
{% test is_even(model, column_name) %}  
  
with validation as (  
  
    select  
        {{ column_name }} as even_field  
  
    from {{ model }}  
  
),  
  
validation_errors as (  
  
    select  
        even_field  
  
    from validation  
    -- if this is true, then even_field is actually odd!  
    where (even_field % 2) = 1  
  
)  
  
select *  
from validation_errors  
  
{% endtest %}
```

If this `select` statement returns zero records, then every record in the supplied `model` argument is even! If a nonzero number of records is returned instead, then at least one record in `model` is odd, and the test has failed.

To use this generic test, specify it by name in the `data_tests` property of a model, source, snapshot, or seed:

With one line of code, you've just created a test! In this example, `users` will be passed to the `is_even` test as the `model` argument, and `favorite_number` will be passed in as the `column_name` argument. You could add the same line for other columns, other models—each will add a new test to your project, *using the same generic test definition*.

### Add description to generic data test logic[​](#add-description-to-generic-data-test-logic "Direct link to Add description to generic data test logic")

You can add a description to the Jinja macro that provides the core logic for a data test by including the `description` key under the `macros:` section. You can add descriptions directly to the macro, including descriptions for macro arguments.

Here's an example:

macros/generic/schema.yml

```
macros:  
  - name: test_not_empty_string  
    description: Complementary test to default `not_null` test as it checks that there is not an empty string. It only accepts columns of type string.  
    arguments:  
      - name: model   
        type: string  
        description: Model Name  
      - name: column_name  
        type: string  
        description: Column name that should not be an empty string
```

In this example:

* When documenting custom test macros in a `schema.yml` file, add the `test_` prefix to the macro name. For example, if the test block's name is `not_empty_string`, then the macro's name would be `test_not_empty_string`.
* We've provided a description at the macro level, explaining what the test does and any relevant notes.
* Each argument (like `model`, `column_name`) also includes a description to clarify its purpose.

### Generic tests with additional arguments[​](#generic-tests-with-additional-arguments "Direct link to Generic tests with additional arguments")

The `is_even` test works without needing to specify any additional arguments. Other tests, like `relationships`, require more than just `model` and `column_name`. If your custom tests requires more than the standard arguments, include those arguments in the test signature, as `field` and `to` are included below:

tests/generic/test\_relationships.sql

```
{% test relationships(model, column_name, field, to) %}  
  
with parent as (  
  
    select  
        {{ field }} as id  
  
    from {{ to }}  
  
),  
  
child as (  
  
    select  
        {{ column_name }} as id  
  
    from {{ model }}  
  
)  
  
select *  
from child  
where id is not null  
  and id not in (select id from parent)  
  
{% endtest %}
```

When calling this test from a `.yml` file, supply the arguments to the test in a dictionary. Note that the standard arguments (`model` and `column_name`) are provided by the context, so you do not need to define them again.

### Generic tests with default config values[​](#generic-tests-with-default-config-values "Direct link to Generic tests with default config values")

It is possible to include a `config()` block in a generic test definition. Values set there will set defaults for all specific instances of that generic test, unless overridden within the specific instance's `.yml` properties.

tests/generic/warn\_if\_odd.sql

```
{% test warn_if_odd(model, column_name) %}  
  
    {{ config(severity = 'warn') }}  
  
    select *  
    from {{ model }}  
    where ({{ column_name }} % 2) = 1  
  
{% endtest %}
```

Any time the `warn_if_odd` test is used, it will *always* have warning-level severity, unless the specific test overrides that value:

### Customizing dbt's built-in tests[​](#customizing-dbts-built-in-tests "Direct link to Customizing dbt's built-in tests")

To change the way a built-in generic test works—whether to add additional parameters, re-write the SQL, or for any other reason—you simply add a test block named `<test_name>` to your own project. dbt will favor your version over the global implementation!

tests/generic/<filename>.sql

```
{% test unique(model, column_name) %}  
  
    -- whatever SQL you'd like!  
  
{% endtest %}
```

### Examples[​](#examples "Direct link to Examples")

Here's some additional examples of custom generic ("schema") tests from the community:

* [Creating a custom schema test with an error threshold](https://discourse.getdbt.com/t/creating-an-error-threshold-for-schema-tests/966)
* [Using custom schema tests to only run tests in production](https://discourse.getdbt.com/t/conditionally-running-dbt-tests-only-running-dbt-tests-in-production/322)
* [Additional examples of custom schema tests](https://discourse.getdbt.com/t/examples-of-custom-schema-tests/181)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/best-practices/custom-generic-tests.md)

Last updated on **Nov 19, 2025**

[Previous

Clone incremental models as the first step of your CI job](/best-practices/clone-incremental-models)[Next

Best practices for workflows](/best-practices/best-practice-workflows)

* [Generic tests with standard arguments](#generic-tests-with-standard-arguments)
* [Add description to generic data test logic](#add-description-to-generic-data-test-logic)
* [Generic tests with additional arguments](#generic-tests-with-additional-arguments)
* [Generic tests with default config values](#generic-tests-with-default-config-values)
* [Customizing dbt's built-in tests](#customizing-dbts-built-in-tests)
* [Examples](#examples)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/best-practices/custom-generic-tests.md)

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