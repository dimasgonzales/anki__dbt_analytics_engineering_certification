# Source: https://docs.getdbt.com/docs/build/dbt-tips

dbt tips and tricks | dbt Developer Hub

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
* dbt tips and tricks

Copy page

On this page

dbt tips and tricks
===================

Use this page for valuable insights and practical advice to enhance your dbt experience. Whether you're new to dbt or an experienced user, these tips are designed to help you work more efficiently and effectively.

The following tips are organized into the following categories:

* [Package tips](#package-tips) to help you streamline your workflow.
* [Advanced tips and techniques](#advanced-tips-and-techniques) to help you get the most out of dbt.

If you're developing with the Studio IDE, you can refer to the [keyboard shortcuts](/docs/cloud/dbt-cloud-ide/keyboard-shortcuts) page to help make development more productive and easier for everyone.

YAML tips[​](#yaml-tips "Direct link to YAML tips")
---------------------------------------------------

This section clarifies where you can use [Jinja](/docs/build/jinja-macros), nest [vars](/reference/dbt-jinja-functions/var) and [`env_var`](/reference/dbt-jinja-functions/env_var) in your YAML files.

* You can use Jinja in almost every YAML file in dbt *except* the [`dependencies.yml` file](/docs/build/packages#use-cases). This is because the `dependencies.yml` file doesn't support Jinja.
* Use `vars` in any YAML file that supports Jinja (like `schema.yml`, `snapshots.yml`). However, note that:
  + In `dbt_project.yml`, `packages.yml`, and `profiles.yml` files, you must pass `vars` through the CLI using `--vars`, not defined inside the `vars:` block in the YAML file. This is because these files are parsed before Jinja is rendered.
* You can use `env_var()` in all YAML files that support Jinja. Only `profiles.yml` and `packages.yml` support environment variables for secure values (using the `DBT_ENV_SECRET_` prefix). These are masked in logs and intended for credentials or secrets.

For additional information, check out [dbt Core's context docs](https://github.com/dbt-labs/dbt-core/blob/main/core/dbt/context/README.md).

Package tips[​](#package-tips "Direct link to Package tips")
------------------------------------------------------------

Leverage these dbt packages to streamline your workflow:

| Package | Description |
| --- | --- |
| [`dbt_codegen`](https://hub.getdbt.com/dbt-labs/codegen/latest/) | Use the package to help you generate YML files for your models and sources and SQL files for your staging models. |
| [`dbt_utils`](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/) | The package contains macros useful for daily development. For example, `date_spine` generates a table with all dates between the ones provided as parameters. |
| [`dbt_project_evaluator`](https://hub.getdbt.com/dbt-labs/dbt_project_evaluator/latest) | The package compares your dbt project against a list of our best practices and provides suggestions and guidelines on how to update your models. |
| [`dbt_expectations`](https://hub.getdbt.com/metaplane/dbt_expectations/latest/) | The package contains many tests beyond those built into dbt. |
| [`dbt_audit_helper`](https://hub.getdbt.com/#:~:text=adwords-,audit_helper,-codegen) | The package lets you compare the output of 2 queries. Use it when refactoring existing logic to ensure that the new results are identical. |
| [`dbt_artifacts`](https://hub.getdbt.com/brooklyn-data/dbt_artifacts/latest) | The package saves information about your dbt runs directly to your data platform so that you can track the performance of models over time. |
| [`dbt_meta_testing`](https://hub.getdbt.com/tnightengale/dbt_meta_testing/latest) | This package checks that your dbt project is sufficiently tested and documented. |

Advanced tips and techniques[​](#advanced-tips-and-techniques "Direct link to Advanced tips and techniques")
------------------------------------------------------------------------------------------------------------

* Use your folder structure as your primary selector method. `dbt build --select marts.marketing` is simpler and more resilient than relying on tagging every model.
* Think about jobs in terms of build cadences and SLAs. Run models that have hourly, daily, or weekly build cadences together.
* Use the [where config](/reference/resource-configs/where) for tests to test an assertion on a subset of records.
* [store\_failures](/reference/resource-configs/store_failures) lets you examine records that cause tests to fail, so you can either repair the data or change the test as needed.
* Use [severity](/reference/resource-configs/severity) thresholds to set an acceptable number of failures for a test.
* Use [incremental\_strategy](/docs/build/incremental-strategy) in your incremental model config to implement the most effective behavior depending on the volume of your data and reliability of your unique keys.
* Set `vars` in your `dbt_project.yml` to define global defaults for certain conditions, which you can then override using the `--vars` flag in your commands.
* Use [for loops](/guides/using-jinja?step=3) in Jinja to DRY up repetitive logic, such as selecting a series of columns that all require the same transformations and naming patterns to be applied.
* Instead of relying on post-hooks, use the [grants config](/reference/resource-configs/grants) to apply permission grants in the warehouse resiliently.
* Define [source-freshness](/docs/build/sources#source-data-freshness) thresholds on your sources to avoid running transformations on data that has already been processed.
* Use the `+` operator on the left of a model `dbt build --select +model_name` to run a model and all of its upstream dependencies. Use the `+` operator on the right of the model `dbt build --select model_name+` to run a model and everything downstream that depends on it.
* Use `dir_name` to run all models in a package or directory.
* Use the `@` operator on the left of a model in a non-state-aware CI setup to test it. This operator runs all of a selection’s parents and children, and also runs the parents of its children, which in a fresh CI schema will likely not exist yet.
* Use the [--exclude flag](/reference/node-selection/exclude) to remove a subset of models out of a selection.
* Use the [--full-refresh](/reference/commands/run#refresh-incremental-models) flag to rebuild an incremental model from scratch.
* Use [seeds](/docs/build/seeds) to create manual lookup tables, like zip codes to states or marketing UTMs to campaigns. `dbt seed` will build these from CSVs into your warehouse and make them `ref` able in your models.
* Use [target.name](/docs/build/custom-schemas#an-alternative-pattern-for-generating-schema-names) to pivot logic based on what environment you’re using. For example, to build into a single development schema while developing, but use multiple schemas in production.

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [Quickstart guide](/guides)
* [About dbt](/docs/cloud/about-cloud/dbt-cloud-features)
* [Develop in the Cloud](/docs/cloud/about-develop-dbt)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/dbt-tips.md)

Last updated on **Nov 19, 2025**

[Previous

About dbt projects](/docs/build/projects)

* [YAML tips](#yaml-tips)
* [Package tips](#package-tips)
* [Advanced tips and techniques](#advanced-tips-and-techniques)
* [Related docs](#related-docs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/dbt-tips.md)

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