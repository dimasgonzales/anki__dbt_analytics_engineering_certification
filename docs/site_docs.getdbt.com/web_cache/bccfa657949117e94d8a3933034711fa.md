# Source: https://docs.getdbt.com/docs/build/custom-schemas

Custom schemas | dbt Developer Hub

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
  + [Build your metrics](/docs/build/build-metrics-intro)
  + [Enhance your models](/docs/build/enhance-your-models)
  + [Enhance your code](/docs/build/enhance-your-code)
  + [Organize your outputs](/docs/build/organize-your-outputs)

    - [Organize your outputs](/docs/build/organize-your-outputs)
    - [Custom schemas](/docs/build/custom-schemas)
    - [Custom databases](/docs/build/custom-databases)
    - [Custom aliases](/docs/build/custom-aliases)
    - [Custom target names](/docs/build/custom-target-names)
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
* [Organize your outputs](/docs/build/organize-your-outputs)
* Custom schemas

Copy page

On this page

Custom schemas
==============

By default, all dbt models are built in the schema specified in your [environment](/docs/dbt-cloud-environments) (dbt) or [profile's target](/docs/core/dbt-core-environments) (dbt Core). This default schema is called your *target schema*.

For dbt projects with lots of models, it's common to build models across multiple schemas and group similar models together. For example, you might want to:

* Group models based on the business unit using the model, creating schemas such as `core`, `marketing`, `finance` and `support`.
* Hide intermediate models in a `staging` schema, and only present models that should be queried by an end user in an `analytics` schema.

To do this, specify a custom schema. dbt generates the schema name for a model by appending the custom schema to the target schema. For example, `<target_schema>_<custom_schema>`.

| Target schema | Custom schema | Resulting schema |
| --- | --- | --- |
| analytics\_prod | None | analytics\_prod |
| alice\_dev | None | alice\_dev |
| dbt\_cloud\_pr\_123\_456 | None | dbt\_cloud\_pr\_123\_456 |
| analytics\_prod | marketing | analytics\_prod\_marketing |
| alice\_dev | marketing | alice\_dev\_marketing |
| dbt\_cloud\_pr\_123\_456 | marketing | dbt\_cloud\_pr\_123\_456\_marketing |

How do I use custom schemas?[​](#how-do-i-use-custom-schemas "Direct link to How do I use custom schemas?")
-----------------------------------------------------------------------------------------------------------

To specify a custom schema for a model, use the `schema` configuration key. As with any configuration, you can do one of the following:

* apply this configuration to a specific model by using a config block within a model
* apply it to a subdirectory of models by specifying it in your `dbt_project.yml` file

orders.sql

```
{{ config(schema='marketing') }}  
  
select ...
```

dbt\_project.yml

```
# models in `models/marketing/ will be built in the "*_marketing" schema  
models:  
  my_project:  
    marketing:  
      +schema: marketing
```

Understanding custom schemas[​](#understanding-custom-schemas "Direct link to Understanding custom schemas")
------------------------------------------------------------------------------------------------------------

When first using custom schemas, it's a common misunderstanding to assume that a model *only* uses the new `schema` configuration; for example, a model that has the configuration `schema: marketing` would be built in the `marketing` schema. However, dbt puts it in a schema like `<target_schema>_marketing`.

There's a good reason for this deviation. Each dbt user has their own target schema for development (refer to [Managing Environments](#managing-environments)). If dbt ignored the target schema and only used the model's custom schema, every dbt user would create models in the same schema and would overwrite each other's work.

By combining the target schema and the custom schema, dbt ensures that objects it creates in your data warehouse don't collide with one another.

If you prefer to use different logic for generating a schema name, you can change the way dbt generates a schema name (see below).

### How does dbt generate a model's schema name?[​](#how-does-dbt-generate-a-models-schema-name "Direct link to How does dbt generate a model's schema name?")

dbt uses a default macro called `generate_schema_name` to determine the name of the schema that a model should be built in.

The following code represents the default macro's logic:

```
{% macro generate_schema_name(custom_schema_name, node) -%}  
  
    {%- set default_schema = target.schema -%}  
    {%- if custom_schema_name is none -%}  
  
        {{ default_schema }}  
  
    {%- else -%}  
  
        {{ default_schema }}_{{ custom_schema_name | trim }}  
  
    {%- endif -%}  
  
{%- endmacro %}
```

  

💡 Use Jinja's whitespace control to tidy your macros!

When you're modifying macros in your project, you might notice extra white space in your code in the `target/compiled` folder.

You can remove unwanted spaces and lines with Jinja's [whitespace control](/faqs/Jinja/jinja-whitespace) by using a minus sign. For example, use `{{- ... -}}` or `{%- ... %}` around your macro definitions (such as `{%- macro generate_schema_name(...) -%} ... {%- endmacro -%}`).

Changing the way dbt generates a schema name[​](#changing-the-way-dbt-generates-a-schema-name "Direct link to Changing the way dbt generates a schema name")
------------------------------------------------------------------------------------------------------------------------------------------------------------

If your dbt project has a custom macro called `generate_schema_name`, dbt will use it instead of the default macro. This allows you to customize the name generation according to your needs.

To customize this macro, copy the example code in the section [How does dbt generate a model's schema name](#how-does-dbt-generate-a-models-schema-name) into a file named `macros/generate_schema_name.sql` and make changes as necessary.

Be careful. dbt will ignore any custom `generate_schema_name` macros included in installed packages.

 Warning: Don't replace `default\_schema` in the macro

If you're modifying how dbt generates schema names, don't just replace `{{ default_schema }}_{{ custom_schema_name | trim }}` with `{{ custom_schema_name | trim }}` in the `generate_schema_name` macro.

If you remove `{{ default_schema }}`, it causes developers to override each other's models if they create their own custom schemas. This can also cause issues during development and continuous integration (CI).

❌ The following code block is an example of what your code *should not* look like:

```
{% macro generate_schema_name(custom_schema_name, node) -%}  
  
    {%- set default_schema = target.schema -%}  
    {%- if custom_schema_name is none -%}  
  
        {{ default_schema }}  
  
    {%- else -%}  
    # The following is incorrect as it omits {{ default_schema }} before {{ custom_schema_name | trim }}.   
        {{ custom_schema_name | trim }}   
  
    {%- endif -%}  
  
{%- endmacro %}
```

### generate\_schema\_name arguments[​](#generate_schema_name-arguments "Direct link to generate_schema_name arguments")

| Argument | Description | Example |
| --- | --- | --- |
| custom\_schema\_name | The configured value of `schema` in the specified node, or `none` if a value is not supplied | `marketing` |
| node | The `node` that is currently being processed by dbt | `{"name": "my_model", "resource_type": "model",...}` |

### Jinja context available in generate\_schema\_name[​](#jinja-context-available-in-generate_schema_name "Direct link to Jinja context available in generate_schema_name")

If you choose to write custom logic to generate a schema name, it's worth noting that not all variables and methods are available to you when defining this logic. In other words: the `generate_schema_name` macro is compiled with a limited Jinja context.

The following context methods *are* available in the `generate_schema_name` macro:

| Jinja context | Type | Available |
| --- | --- | --- |
| [target](/reference/dbt-jinja-functions/target) | Variable | ✅ |
| [env\_var](/reference/dbt-jinja-functions/env_var) | Variable | ✅ |
| [var](/reference/dbt-jinja-functions/var) | Variable | Limited, see below |
| [exceptions](/reference/dbt-jinja-functions/exceptions) | Macro | ✅ |
| [log](/reference/dbt-jinja-functions/log) | Macro | ✅ |
| Other macros in your project | Macro | ✅ |
| Other macros in your packages | Macro | ✅ |

### Which vars are available in generate\_schema\_name?[​](#which-vars-are-available-in-generate_schema_name "Direct link to Which vars are available in generate_schema_name?")

Globally-scoped variables and variables defined on the command line with
[--vars](/docs/build/project-variables) are accessible in the `generate_schema_name` context.

### Managing different behaviors across packages[​](#managing-different-behaviors-across-packages "Direct link to Managing different behaviors across packages")

See docs on macro `dispatch`: ["Managing different global overrides across packages"](/reference/dbt-jinja-functions/dispatch)

A built-in alternative pattern for generating schema names[​](#a-built-in-alternative-pattern-for-generating-schema-names "Direct link to A built-in alternative pattern for generating schema names")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A common customization is to use the custom schema in production when provided, with the target schema serving only as a fallback if no custom schema is specified. In other environments, such as development and CI, custom schema configurations are ignored, defaulting to the target schema instead.

Production Environment (`target.name == 'prod'`)

| Target schema | Custom schema | Resulting schema |
| --- | --- | --- |
| analytics\_prod | None | analytics\_prod |
| analytics\_prod | marketing | marketing |

Development/CI Environment (`target.name != 'prod'`)

| Target schema | Custom schema | Resulting schema |
| --- | --- | --- |
| alice\_dev | None | alice\_dev |
| alice\_dev | marketing | alice\_dev |
| dbt\_cloud\_pr\_123\_456 | None | dbt\_cloud\_pr\_123\_456 |
| dbt\_cloud\_pr\_123\_456 | marketing | dbt\_cloud\_pr\_123\_456 |

Similar to the regular macro, this approach guarantees that schemas from different environments will not collide.

dbt ships with a macro for this use case — called `generate_schema_name_for_env` — which is disabled by default. To enable it, add a custom `generate_schema_name` macro to your project that contains the following code:

macros/get\_custom\_schema.sql

```
-- put this in macros/get_custom_schema.sql  
  
{% macro generate_schema_name(custom_schema_name, node) -%}  
    {{ generate_schema_name_for_env(custom_schema_name, node) }}  
{%- endmacro %}
```

When using this macro, you'll need to set the target name in your production job to `prod`.

Managing environments[​](#managing-environments "Direct link to Managing environments")
---------------------------------------------------------------------------------------

In the `generate_schema_name` macro examples shown in the [built-in alternative pattern](#a-built-in-alternative-pattern-for-generating-schema-names) section, the `target.name` context variable is used to change the schema name that dbt generates for models. If the `generate_schema_name` macro in your project uses the `target.name` context variable, you must ensure that your different dbt environments are configured accordingly. While you can use any naming scheme you'd like, we typically recommend:

* **dev** — Your local development environment; configured in a `profiles.yml` file on your computer.
* **ci** — A [continuous integration](/docs/cloud/git/connect-github) environment running on pull requests in GitHub, GitLab, and so on.
* **prod** — The production deployment of your dbt project, like in dbt, Airflow, or [similar](/docs/deploy/deployments).

If your schema names are being generated incorrectly, double-check your target name in the relevant environment.

For more information, consult the [managing environments in dbt Core](/docs/core/dbt-core-environments) guide.

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [Customize dbt models database, schema, and alias](/guides/customize-schema-alias?step=1) to learn how to customize dbt models database, schema, and alias
* [Custom database](/docs/build/custom-databases) to learn how to customize dbt model database
* [Custom aliases](/docs/build/custom-aliases) to learn how to customize dbt model alias name

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/custom-schemas.md)

Last updated on **Nov 19, 2025**

[Previous

Organize your outputs](/docs/build/organize-your-outputs)[Next

Custom databases](/docs/build/custom-databases)

* [How do I use custom schemas?](#how-do-i-use-custom-schemas)
* [Understanding custom schemas](#understanding-custom-schemas)
  + [How does dbt generate a model's schema name?](#how-does-dbt-generate-a-models-schema-name)
* [Changing the way dbt generates a schema name](#changing-the-way-dbt-generates-a-schema-name)
  + [generate\_schema\_name arguments](#generate_schema_name-arguments)
  + [Jinja context available in generate\_schema\_name](#jinja-context-available-in-generate_schema_name)
  + [Which vars are available in generate\_schema\_name?](#which-vars-are-available-in-generate_schema_name)
  + [Managing different behaviors across packages](#managing-different-behaviors-across-packages)
* [A built-in alternative pattern for generating schema names](#a-built-in-alternative-pattern-for-generating-schema-names)
* [Managing environments](#managing-environments)
* [Related docs](#related-docs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/custom-schemas.md)

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