# Source: https://docs.getdbt.com/reference/node-selection/test-selection-examples

Test selection examples | dbt Developer Hub

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
* [Commands](/reference/dbt-commands)

  + [dbt Command reference](/reference/dbt-commands)
  + [List of commands](/category/list-of-commands)
  + [Node selection](/reference/node-selection/syntax)

    - [Syntax overview](/reference/node-selection/syntax)
    - [Exclude](/reference/node-selection/exclude)
    - [Defer](/reference/node-selection/defer)
    - [Graph operators](/reference/node-selection/graph-operators)
    - [Set operators](/reference/node-selection/set-operators)
    - [Node selector methods](/reference/node-selection/methods)
    - [Putting it together](/reference/node-selection/putting-it-together)
    - [YAML Selectors](/reference/node-selection/yaml-selectors)
    - [Test selection examples](/reference/node-selection/test-selection-examples)
    - [About state selection](/reference/node-selection/state-selection)
  + [Flags (global configs)](/reference/global-configs/about-global-configs)
  + [Events and logs](/reference/events-logging)
  + [Exit codes](/reference/exit-codes)
  + [Deprecations](/reference/deprecations)
  + [Project Parsing](/reference/parsing)
  + [Programmatic invocations](/reference/programmatic-invocations)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Commands](/reference/dbt-commands)
* [Node selection](/reference/node-selection/syntax)
* Test selection examples

Copy page

On this page

Test selection examples
=======================

Test selection works a little differently from other resource selection. This makes it very easy to:

* run tests on a particular model
* run tests on all models in a subdirectory
* run tests on all models upstream / downstream of a model, etc.

Like all resource types, tests can be selected **directly**, by methods and operators that capture one of their attributes: their name, properties, tags, etc.

Unlike other resource types, tests can also be selected **indirectly**. If a selection method or operator includes a test's parent(s), the test will also be selected. [See below](#indirect-selection) for more details.

Test selection is powerful, and we know it can be tricky. To that end, we've included lots of examples below:

### Direct selection[​](#direct-selection "Direct link to Direct selection")

Run generic tests only:

```
  dbt test --select "test_type:generic"
```

Run singular tests only:

```
  dbt test --select "test_type:singular"
```

In both cases, `test_type` checks a property of the test itself. These are forms of "direct" test selection.

### Indirect selection[​](#indirect-selection "Direct link to Indirect selection")

You can use the following modes to configure the behavior when performing indirect selection (with `eager` mode as the default). Test exclusion is always greedy: if ANY parent is explicitly excluded, the test will be excluded as well.

Building subsets of a DAG

The `buildable` and `cautious` modes can be useful when you're only building a subset of your DAG, and you want to avoid test failures in `eager` mode caused by unbuilt resources. You can also achieve this with [deferral](/reference/node-selection/defer).

#### Eager mode[​](#eager-mode "Direct link to Eager mode")

By default, runs tests if any of the parent nodes are selected, regardless of whether all dependencies are met. This includes ANY tests that reference the selected nodes. Models will be built if they depend on the selected model. In this mode, any tests depending on unbuilt resources will raise an error.

#### Buildable mode[​](#buildable-mode "Direct link to Buildable mode")

Only runs tests that refer to selected nodes (or their ancestors). This mode is slightly more inclusive than `cautious` by including tests whose references are each within the selected nodes (or their ancestors). This mode is useful when a test depends on a model *and* a direct ancestor of that model, like confirming an aggregation has the same totals as its input.

#### Cautious mode[​](#cautious-mode "Direct link to Cautious mode")

Ensures that tests are executed and models are built only when all necessary dependencies of the selected models are met. Restricts tests to only those that exclusively reference selected nodes. Tests will only be executed if all the nodes they depend on are selected, which prevents tests from running if one or more of its parent nodes are unselected and, consequently, unbuilt.

#### Empty mode[​](#empty-mode "Direct link to Empty mode")

Restricts the build to only the selected node and ignores any indirect dependencies, including tests. It doesn't execute any tests, whether they are directly attached to the selected node or not. The empty mode does not include any tests and is automatically used for [interactive compilation](/reference/commands/compile#interactive-compile).

### Indirect selection examples[​](#indirect-selection-examples "Direct link to Indirect selection examples")

To visualize these methods, suppose you have `model_a`, `model_b`, and `model_c` and associated data tests. The following illustrates which tests will be run when you execute `dbt build` with the various indirect selection modes:

[![dbt build](/img/docs/reference/indirect-selection-dbt-build.png?v=2 "dbt build")](#)dbt build

[![Eager (default)](/img/docs/reference/indirect-selection-eager.png?v=2 "Eager (default)")](#)Eager (default)

[![Buildable](/img/docs/reference/indirect-selection-buildable.png?v=2 "Buildable")](#)Buildable

[![Cautious](/img/docs/reference/indirect-selection-cautious.png?v=2 "Cautious")](#)Cautious

[![Empty](/img/docs/reference/indirect-selection-empty.png?v=2 "Empty")](#)Empty

* Eager mode (default)
* Buildable mode
* Cautious mode
* Empty mode

In this example, during the build process, any test that depends on the selected "orders" model or its dependent models will be executed, even if it depends other models as well.

```
dbt test --select "orders"  
dbt build --select "orders"
```

In this example, dbt executes tests that reference "orders" within the selected nodes (or their ancestors).

```
dbt test --select "orders" --indirect-selection=buildable  
dbt build --select "orders" --indirect-selection=buildable
```

In this example, only tests that depend *exclusively* on the "orders" model will be executed:

```
dbt test --select "orders" --indirect-selection=cautious  
dbt build --select "orders" --indirect-selection=cautious
```

This mode does not execute any tests, whether they are directly attached to the selected node or not.

```
dbt test --select "orders" --indirect-selection=empty  
dbt build --select "orders" --indirect-selection=empty
```

### Test selection syntax examples[​](#test-selection-syntax-examples "Direct link to Test selection syntax examples")

Setting `indirect_selection` can also be specified in a [yaml selector](/reference/node-selection/yaml-selectors#indirect-selection).

The following examples should feel somewhat familiar if you're used to executing `dbt run` with the `--select` option to build parts of your DAG:

```
# Run tests on a model (indirect selection)  
dbt test --select "customers"  
  
# Run tests on two or more specific models (indirect selection)  
dbt test --select "customers orders"  
  
# Run tests on all models in the models/staging/jaffle_shop directory (indirect selection)  
dbt test --select "staging.jaffle_shop"  
  
# Run tests downstream of a model (note this will select those tests directly!)  
dbt test --select "stg_customers+"  
  
# Run tests upstream of a model (indirect selection)  
dbt test --select "+stg_customers"  
  
# Run tests on all models with a particular tag (direct + indirect)  
dbt test --select "tag:my_model_tag"  
  
# Run tests on all models with a particular materialization (indirect selection)  
dbt test --select "config.materialized:table"
```

The same principle can be extended to tests defined on other resource types. In these cases, we will execute all tests defined on certain sources via the `source:` selection method:

```
# tests on all sources  
  
dbt test --select "source:*"  
  
# tests on one source  
dbt test --select "source:jaffle_shop"  
  
# tests on two or more specific sources  
 dbt test --select "source:jaffle_shop source:raffle_bakery"  
  
# tests on one source table  
dbt test --select "source:jaffle_shop.customers"  
  
# tests on everything _except_ sources  
dbt test --exclude "source:*"
```

### More complex selection[​](#more-complex-selection "Direct link to More complex selection")

Through the combination of direct and indirect selection, there are many ways to accomplish the same outcome. Let's say we have a data test named `assert_total_payment_amount_is_positive` that depends on a model named `payments`. All of the following would manage to select and execute that test specifically:

```
dbt test --select "assert_total_payment_amount_is_positive" # directly select the test by name  
dbt test --select "payments,test_type:singular" # indirect selection, v1.2
```

As long as you can select a common property of a group of resources, indirect selection allows you to execute all the tests on those resources, too. In the example above, we saw it was possible to test all table-materialized models. This principle can be extended to other resource types, too:

```
# Run tests on all models with a particular materialization  
dbt test --select "config.materialized:table"  
  
# Run tests on all seeds, which use the 'seed' materialization  
dbt test --select "config.materialized:seed"  
  
# Run tests on all snapshots, which use the 'snapshot' materialization  
dbt test --select "config.materialized:snapshot"
```

Note that this functionality may change in future versions of dbt.

### Run tests on tagged columns[​](#run-tests-on-tagged-columns "Direct link to Run tests on tagged columns")

Because the column `order_id` is tagged `my_column_tag`, the test itself also receives the tag `my_column_tag`. Because of that, this is an example of direct selection.

models/<filename>.yml

```
models:  
  - name: orders  
    columns:  
      - name: order_id  
        config:  
          tags: [my_column_tag] # changed to config in v1.10 and backported to 1.9  
        data_tests:  
          - unique
```

```
dbt test --select "tag:my_column_tag"
```

Currently, tests "inherit" tags applied to columns, sources, and source tables. They do *not* inherit tags applied to models, seeds, or snapshots. In all likelihood, those tests would still be selected indirectly, because the tag selects its parent. This is a subtle distinction, and it may change in future versions of dbt.

### Run tagged tests only[​](#run-tagged-tests-only "Direct link to Run tagged tests only")

This is an even clearer example of direct selection: the test itself is tagged `my_test_tag`, and selected accordingly.

models/<filename>.yml

```
models:  
  - name: orders  
    columns:  
      - name: order_id  
        data_tests:  
          - unique:  
            config:  
              tags: [my_test_tag] # changed to config in v1.10
```

```
dbt test --select "tag:my_test_tag"
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/node-selection/test-selection-examples.md)

Last updated on **Nov 19, 2025**

[Previous

YAML Selectors](/reference/node-selection/yaml-selectors)[Next

About state in dbt](/reference/node-selection/state-selection)

* [Direct selection](#direct-selection)
* [Indirect selection](#indirect-selection)
* [Indirect selection examples](#indirect-selection-examples)
* [Test selection syntax examples](#test-selection-syntax-examples)
* [More complex selection](#more-complex-selection)
* [Run tests on tagged columns](#run-tests-on-tagged-columns)
* [Run tagged tests only](#run-tagged-tests-only)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/node-selection/test-selection-examples.md)

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