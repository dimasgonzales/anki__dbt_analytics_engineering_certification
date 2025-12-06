# Source: https://docs.getdbt.com/reference/resource-properties/description

description | dbt Developer Hub

[Skip to main content](#__docusaurus_skipToContent_fallback)

[✨ Live virtual event - Smarter pipelines, 29% more efficient: How the dbt Fusion engine optimizes data work on December 3rd!](https://www.getdbt.com/resources/webinars/how-the-dbt-fusion-engine-optimizes-data-work)

[![dbt Logo](/img/dbt-logo.svg?v=2)](/)

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

[dbt platform (Latest)](#)

* dbt platform (Latest)
* dbt Fusion engine
* Core v1.11 Beta
* Core v1.10 (Compatible)
* Core v1.9 (Extended)

Search`⌘``K`

[![dbt Logo](/img/dbt-logo.svg?v=2)](/)

* [About References](/reference/references-overview)
* [Project configs](/category/project-configs)
* [Platform-specific configs](/reference/resource-configs/resource-configs)
* [Resource configs and properties](/reference/resource-configs/resource-path)

  + [About resource paths](/reference/resource-configs/resource-path)
  + [Configs and properties](/reference/configs-and-properties)
  + [General properties](/category/general-properties)

    - [anchors](/reference/resource-properties/anchors)
    - [columns](/reference/resource-properties/columns)
    - [config](/reference/resource-properties/config)
    - [constraints](/reference/resource-properties/constraints)
    - [deprecation\_date](/reference/resource-properties/deprecation_date)
    - [description](/reference/resource-properties/description)
    - [latest\_version](/reference/resource-properties/latest_version)
    - [Data tests](/reference/resource-properties/data-tests)
    - [versions](/reference/resource-properties/versions)
  + [General configs](/category/general-configs)
  + [For models](/reference/model-properties)
  + [For seeds](/reference/seed-properties)
  + [For snapshots](/reference/snapshot-properties)
  + [For data tests](/reference/data-test-configs)
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
* [General properties](/category/general-properties)
* description

Copy page

On this page

description
===========

* Models
* Sources
* Seeds
* Snapshots
* Analyses
* Macros
* Data tests
* Unit tests

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

* [Add a simple description to a model and column](#add-a-simple-description-to-a-model-and-column)
* [Add a multiline description to a model](#add-a-multiline-description-to-a-model)
* [Use some markdown in a description](#use-some-markdown-in-a-description)
* [Use a docs block in a description](#use-a-docs-block-in-a-description)
* [Link to another model in a description](#link-to-another-model-in-a-description)
* [Include an image from your repo in your descriptions](#include-an-image-from-your-repo-in-your-descriptions)
* [Include an image from the web in your descriptions](#include-an-image-from-the-web-in-your-descriptions)
* [Add a description to a data test](#add-a-description-to-a-data-test)
* [Add a description to a unit test](#add-a-description-to-a-unit-test)

### Add a simple description to a model and column[​](#add-a-simple-description-to-a-model-and-column "Direct link to Add a simple description to a model and column")

models/schema.yml

```
version: 2  
  
models:  
  - name: dim_customers  
    description: One record per customer  
  
    columns:  
      - name: customer_id  
        description: Primary key
```

### Add a multiline description to a model[​](#add-a-multiline-description-to-a-model "Direct link to Add a multiline description to a model")

You can use YAML [block notation](https://yaml-multiline.info/) to split a longer description over multiple lines:

models/schema.yml

```
version: 2  
  
models:  
  - name: dim_customers  
    description: >  
      One record per customer. Note that a customer must have made a purchase to  
      be included in this <Term id="table" /> — customer accounts that were created but never  
      used have been filtered out.  
  
    columns:  
      - name: customer_id  
        description: Primary key.
```

### Use some markdown in a description[​](#use-some-markdown-in-a-description "Direct link to Use some markdown in a description")

You can use markdown in your descriptions, but you may need to quote your description to ensure the YAML parser doesn't get confused by special characters!

models/schema.yml

```
version: 2  
  
models:  
  - name: dim_customers  
    description: "**[Read more](https://www.google.com/)**"  
  
    columns:  
      - name: customer_id  
        description: Primary key.
```

### Use a docs block in a description[​](#use-a-docs-block-in-a-description "Direct link to Use a docs block in a description")

If you have a long description, especially if it contains markdown, it may make more sense to leverage a [`docs` block](/reference/dbt-jinja-functions/doc). A benefit of this approach is that code editors will correctly highlight markdown, making it easier to debug as you write.

models/schema.yml

```
version: 2  
  
models:  
  - name: fct_orders  
    description: This table has basic information about orders, as well as some derived facts based on payments  
  
    columns:  
      - name: status  
        description: '{{ doc("orders_status") }}'
```

models/docs.md

```
{% docs orders_status %}  
  
Orders can be one of the following statuses:  
  
| status         | description                                                               |  
|----------------|---------------------------------------------------------------------------|  
| placed         | The order has been placed but has not yet left the warehouse              |  
| shipped        | The order has been shipped to the customer and is currently in transit     |  
| completed      | The order has been received by the customer                               |  
| returned       | The order has been returned by the customer and received at the warehouse |  
  
  
{% enddocs %}
```

### Link to another model in a description[​](#link-to-another-model-in-a-description "Direct link to Link to another model in a description")

You can use relative links to link to another model. It's a little hacky — but to do this:

1. Serve your docs site.
2. Navigate to the model you want to link to, e.g. `http://127.0.0.1:8080/#!/model/model.jaffle_shop.stg_stripe__payments`
3. Copy the url\_path, i.e. everything after `http://127.0.0.1:8080/`, so in this case `#!/model/model.jaffle_shop.stg_stripe__payments`
4. Paste it as the link

models/schema.yml

```
version: 2  
  
models:  
  - name: customers  
    description: "Filtering done based on [stg_stripe__payments](#!/model/model.jaffle_shop.stg_stripe__payments)"  
  
    columns:  
      - name: customer_id  
        description: Primary key
```

### Include an image from your repo in your descriptions[​](#include-an-image-from-your-repo-in-your-descriptions "Direct link to Include an image from your repo in your descriptions")

This section applies to dbt Core users only. Including an image from your repository ensures your images are version-controlled.

Both dbt and dbt Core users can [include an image from the web](#include-an-image-from-the-web-in-your-descriptions), which offers dynamic content, reduced repository size, accessibility, and ease of collaboration.

To include an image in your model's `description` field:

1. Add the file in a subdirectory, e.g. `assets/dbt-logo.svg`
2. Set the [`asset-paths` config](/reference/project-configs/asset-paths) in your `dbt_project.yml` file so that this directory gets copied to the `target/` directory as part of `dbt docs generate`

dbt\_project.yml

```
asset-paths: ["assets"]
```

2. Use a Markdown link to the image in your `description:`

models/schema.yml

```
version: 2  
  
models:  
  - name: customers  
    description: "![dbt Logo](assets/dbt-logo.svg)"  
  
    columns:  
      - name: customer_id  
        description: Primary key
```

3. Run `dbt docs generate` — the `assets` directory will be copied to the `target` directory
4. Run `dbt docs serve` — the image will be rendered as part of your project documentation:

If mixing images and text, also consider using a docs block.

### Include an image from the web in your descriptions[​](#include-an-image-from-the-web-in-your-descriptions "Direct link to Include an image from the web in your descriptions")

This section applies to dbt and dbt Core users. Including an image from the web offers dynamic content, reduced repository size, accessibility, and ease of collaboration.

To include images from the web, specify the image URL in your model's `description` field:

models/schema.yml

```
version: 2  
  
models:  
  - name: customers  
    description: "![dbt Logo](https://github.com/dbt-labs/dbt-core/blob/main/etc/dbt-core.svg)"  
  
    columns:  
      - name: customer_id  
        description: Primary key
```

If mixing images and text, also consider using a docs block.

### Add a description to a data test[​](#add-a-description-to-a-data-test "Direct link to Add a description to a data test")

You can add a `description` property to a generic or singular data test.

#### Generic data test[​](#generic-data-test "Direct link to Generic data test")

This example shows a generic data test that checks for unique values in a column for the `orders` model.

models/<filename>.yml

```
version: 2  
  
models:  
  - name: orders  
    columns:  
      - name: order_id  
        data_tests:  
          - unique:  
              description: "The order_id is unique for every row in the orders model"
```

You can also add descriptions to the Jinja macro that provides the core logic of a generic data test. Refer to the [Add description to generic data test logic](/best-practices/writing-custom-generic-tests#add-description-to-generic-data-test-logic) for more information.

#### Singular data test[​](#singular-data-test "Direct link to Singular data test")

This example shows a singular data test that checks to ensure all values in the `payments` model are not negative (≥ 0).

tests/<filename>.yml

```
data_tests:  
  - name: assert_total_payment_amount_is_positive  
    description: >  
      Refunds have a negative amount, so the total amount should always be >= 0.  
      Therefore return records where total amount < 0 to make the test fail.
```

Note that in order for the test to run, the `tests/assert_total_payment_amount_is_positive.sql` SQL file has to exist in the `tests` directory.

### Add a description to a unit test[​](#add-a-description-to-a-unit-test "Direct link to Add a description to a unit test")

This example shows a unit test that checks to ensure the `opened_at` timestamp is properly truncated to a date for the `stg_locations` model.

models/<filename>.yml

```
unit_tests:  
  - name: test_does_location_opened_at_trunc_to_date  
    description: "Check that opened_at timestamp is properly truncated to a date."  
    model: stg_locations  
    given:  
      - input: source('ecom', 'raw_stores')  
        rows:  
          - {id: 1, name: "Rego Park", tax_rate: 0.2, opened_at: "2016-09-01T00:00:00"}  
          - {id: 2, name: "Jamaica", tax_rate: 0.1, opened_at: "2079-10-27T23:59:59.9999"}  
    expect:  
      rows:  
        - {location_id: 1, location_name: "Rego Park", tax_rate: 0.2, opened_date: "2016-09-01"}  
        - {location_id: 2, location_name: "Jamaica", tax_rate: 0.1, opened_date: "2079-10-27"}
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-properties/description.md)

Last updated on **Nov 19, 2025**

[Previous

deprecation\_date](/reference/resource-properties/deprecation_date)[Next

latest\_version](/reference/resource-properties/latest_version)

* [Definition[​](#definition "Direct link to Definition")](#definition)
* [Examples[​](#examples "Direct link to Examples")](#examples)
  + [Add a simple description to a model and column[​](#add-a-simple-description-to-a-model-and-column "Direct link to Add a simple description to a model and column")](#add-a-simple-description-to-a-model-and-column)
  + [Add a multiline description to a model[​](#add-a-multiline-description-to-a-model "Direct link to Add a multiline description to a model")](#add-a-multiline-description-to-a-model)
  + [Use some markdown in a description[​](#use-some-markdown-in-a-description "Direct link to Use some markdown in a description")](#use-some-markdown-in-a-description)
  + [Use a docs block in a description[​](#use-a-docs-block-in-a-description "Direct link to Use a docs block in a description")](#use-a-docs-block-in-a-description)
  + [Link to another model in a description[​](#link-to-another-model-in-a-description "Direct link to Link to another model in a description")](#link-to-another-model-in-a-description)
  + [Include an image from your repo in your descriptions[​](#include-an-image-from-your-repo-in-your-descriptions "Direct link to Include an image from your repo in your descriptions")](#include-an-image-from-your-repo-in-your-descriptions)
  + [Include an image from the web in your descriptions[​](#include-an-image-from-the-web-in-your-descriptions "Direct link to Include an image from the web in your descriptions")](#include-an-image-from-the-web-in-your-descriptions)
  + [Add a description to a data test[​](#add-a-description-to-a-data-test "Direct link to Add a description to a data test")](#add-a-description-to-a-data-test)
  + [Add a description to a unit test[​](#add-a-description-to-a-unit-test "Direct link to Add a description to a unit test")](#add-a-description-to-a-unit-test)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-properties/description.md)

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