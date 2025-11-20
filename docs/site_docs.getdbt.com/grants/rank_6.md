# Source: https://docs.getdbt.com/reference/node-selection/methods

Node selector methods | dbt Developer Hub

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
* Node selector methods

Copy page

On this page

Node selector methods
=====================

Selector methods return all resources that share a common property, using the
syntax `method:value`. While it is recommended to explicitly denote the method,
you can omit it (the default value will be one of `path`, `file` or `fqn`).

 Differences between --select and --selector

The `--select` and `--selector` arguments sound similar, but they are different. To understand the difference, see [Differences between `--select` and `--selector`](/reference/node-selection/yaml-selectors#difference-between---select-and---selector).



tip

You can combine multiple selector methods in one `--select` command by separating them with commas (`,`) without whitespace (for example, `dbt run --select "marts.finance,tag:nightly"`). This only selects resources that satisfy *all* arguments. In this example, the command runs models that are in the `marts/finance` subdirectory and tagged `nightly`. For more information, see [Set operators](/reference/node-selection/set-operators).

Many of the methods below support Unix-style wildcards:

| Wildcard | Description |
| --- | --- |
| \* | matches any number of any characters (including none) |
| ? | matches any single character |
| [abc] | matches one character given in the bracket |
| [a-z] | matches one character from the range given in the bracket |

For example:

```
dbt list --select "*.folder_name.*"  
dbt list --select "package:*_source"
```

### access[​](#access "Direct link to access")

The `access` method selects models based on their [access](/reference/resource-configs/access) property.

```
dbt list --select "access:public"      # list all public models  
dbt list --select "access:private"       # list all private models  
dbt list --select "access:protected"       # list all protected models
```

### config[​](#config "Direct link to config")

The `config` method is used to select models that match a specified [node config](/reference/configs-and-properties).

```
dbt run --select "config.materialized:incremental"    # run all models that are materialized incrementally  
dbt run --select "config.schema:audit"              # run all models that are created in the `audit` schema  
dbt run --select "config.cluster_by:geo_country"      # run all models clustered by `geo_country`
```

While most config values are strings, you can also use the `config` method to match boolean configs, dictionary keys, and values in lists.

For example, given a model with the following configurations:

```
{{ config(  
  materialized = 'incremental',  
  unique_key = ['column_a', 'column_b'],  
  grants = {'select': ['reporter', 'analysts']},  
  meta = {"contains_pii": true},  
  transient = true  
) }}  
  
select ...
```

You can select using any of the following:

```
dbt ls -s config.materialized:incremental  
dbt ls -s config.unique_key:column_a  
dbt ls -s config.grants.select:reporter  
dbt ls -s config.meta.contains_pii:true  
dbt ls -s config.transient:true
```

### exposure[​](#exposure "Direct link to exposure")

The `exposure` method is used to select parent resources of a specified [exposure](/docs/build/exposures). Use in conjunction with the `+` operator.

```
dbt run --select "+exposure:weekly_kpis"                # run all models that feed into the weekly_kpis exposure  
dbt test --select "+exposure:*"                         # test all resources upstream of all exposures  
dbt ls --select "+exposure:*" --resource-type source    # list all source tables upstream of all exposures
```

### file[​](#file "Direct link to file")



### fqn[​](#fqn "Direct link to fqn")

The `fqn` method is used to select nodes based off their "fully qualified names" (FQN) within the dbt graph. The default output of [`dbt list`](/reference/commands/list) is a listing of FQN. The default FQN format is composed of the project name, subdirectories within the path, and the file name (without extension) separated by periods.

```
dbt run --select "fqn:some_model"  
dbt run --select "fqn:your_project.some_model"  
dbt run --select "fqn:some_package.some_other_model"  
dbt run --select "fqn:some_path.some_model"  
dbt run --select "fqn:your_project.some_path.some_model"
```

### group[​](#group "Direct link to group")

The `group` method is used to select models defined within a [group](/reference/resource-configs/group).

```
dbt run --select "group:finance" # run all models that belong to the finance group.
```

### metric[​](#metric "Direct link to metric")

The `metric` method is used to select parent resources of a specified [metric](/docs/build/build-metrics-intro). Use in conjunction with the `+` operator.

```
dbt build --select "+metric:weekly_active_users"       # build all resources upstream of weekly_active_users metric  
dbt ls    --select "+metric:*" --resource-type source  # list all source tables upstream of all metrics
```

### package[​](#package "Direct link to package")

The `package` method is used to select models defined within the root project
or an installed dbt package. While the `package:` prefix is not explicitly required, it may be used to make
selectors unambiguous.

```
# These three selectors are equivalent  
dbt run --select "package:snowplow"  
dbt run --select "snowplow"  
dbt run --select "snowplow.*"
```

Use the `this` package to select nodes from the current project. From the example, running `dbt run --select "package:this"` from the `snowplow` project runs the exact same set of models as the other three selectors.

Since `this` always refers to the current project, using `package:this` ensures that you're only selecting models from the project you're working in.

### path[​](#path "Direct link to path")



### resource\_type[​](#resource_type "Direct link to resource_type")



### result[​](#result "Direct link to result")

The `result` method is related to the [`state` method](/reference/node-selection/methods#state) and can be used to select resources based on their result status from a prior run. Note that one of the dbt commands [`run`, `test`, `build`, `seed`] must have been performed in order to create the result on which a result selector operates.

You can use `result` selectors in conjunction with the `+` operator.

```
# run all models that generated errors on the prior invocation of dbt run  
dbt run --select "result:error" --state path/to/artifacts   
  
# run all tests that failed on the prior invocation of dbt test  
dbt test --select "result:fail" --state path/to/artifacts   
  
# run all the models associated with failed tests from the prior invocation of dbt build  
dbt build --select "1+result:fail" --state path/to/artifacts  
  
# run all seeds that generated errors on the prior invocation of dbt seed  
dbt seed --select "result:error" --state path/to/artifacts
```

* Only use `result:fail` when you want to re-run tests that failed during the last invocation. This selector is specific to test nodes. Tests don't have downstream nodes in the DAG, so using the `result:fail+` selector will only return the failed test itself and not the model or anything built on top of it.
* On the other hand, `result:error` selects any resource (models, tests, snapshots, and more) that returned an error.
* As an example, to re-run upstream and downstream resources associated with failed tests, you can use one of the following selectors:

  ```
  # reruns all the models associated with failed tests from the prior invocation of dbt build  
  dbt build --select "1+result:fail" --state path/to/artifacts  
    
  # reruns the models associated with failed tests and all downstream dependencies - especially useful in deferred state workflows  
  dbt build --select "1+result:fail+" --state path/to/artifacts
  ```

### saved\_query[​](#saved_query "Direct link to saved_query")

The `saved_query` method selects [saved queries](/docs/build/saved-queries).

```
dbt list --select "saved_query:*"                    # list all saved queries   
dbt list --select "+saved_query:orders_saved_query"  # list your saved query named "orders_saved_query" and all upstream resources
```

### semantic\_model[​](#semantic_model "Direct link to semantic_model")

The `semantic_model` method selects [semantic models](/docs/build/semantic-models).

```
dbt list --select "semantic_model:*"        # list all semantic models   
dbt list --select "+semantic_model:orders"  # list your semantic model named "orders" and all upstream resources
```

### source[​](#source "Direct link to source")

The `source` method is used to select models that select from a specified [source](/docs/build/sources#using-sources). Use in conjunction with the `+` operator.

```
dbt run --select "source:snowplow+"    # run all models that select from Snowplow sources
```

### source\_status[​](#source_status "Direct link to source_status")

Another element of job state is the `source_status` of a prior dbt invocation. After executing `dbt source freshness`, for example, dbt creates the `sources.json` artifact which contains execution times and `max_loaded_at` dates for dbt sources. You can read more about `sources.json` on the ['sources'](/reference/artifacts/sources-json) page.

The following dbt commands produce `sources.json` artifacts whose results can be referenced in subsequent dbt invocations:

* `dbt source freshness`

After issuing one of the above commands, you can reference the source freshness results by adding a selector to a subsequent command as follows:

```
# You can also set the DBT_STATE environment variable instead of the --state flag.  
dbt source freshness # must be run again to compare current to previous state  
dbt build --select "source_status:fresher+" --state path/to/prod/artifacts
```

### state[​](#state "Direct link to state")

**N.B.** [State-based selection](/reference/node-selection/state-selection) is a powerful, complex feature. Read about [known caveats and limitations](/reference/node-selection/state-comparison-caveats) to state comparison.

The `state` method is used to select nodes by comparing them against a previous version of the same project, which is represented by a [manifest](/reference/artifacts/manifest-json). The file path of the comparison manifest *must* be specified via the `--state` flag or `DBT_STATE` environment variable.

`state:new`: There is no node with the same `unique_id` in the comparison manifest

`state:modified`: All new nodes, plus any changes to existing nodes.

```
dbt test --select "state:new" --state path/to/artifacts      # run all tests on new models + and new tests on old models  
dbt run --select "state:modified" --state path/to/artifacts  # run all models that have been modified  
dbt ls --select "state:modified" --state path/to/artifacts   # list all modified nodes (not just models)
```

Because state comparison is complex, and everyone's project is different, dbt supports subselectors that include a subset of the full `modified` criteria:

* `state:modified.body`: Changes to node body (e.g. model SQL, seed values)
* `state:modified.configs`: Changes to any node configs, excluding `database`/`schema`/`alias`
* `state:modified.relation`: Changes to `database`/`schema`/`alias` (the database representation of this node), irrespective of `target` values or `generate_x_name` macros
* `state:modified.persisted_descriptions`: Changes to relation- or column-level `description`, *if and only if* `persist_docs` is enabled at each level
* `state:modified.macros`: Changes to upstream macros (whether called directly or indirectly by another macro)
* `state:modified.contract`: Changes to a model's [contract](/reference/resource-configs/contract), which currently include the `name` and `data_type` of `columns`. Removing or changing the type of an existing column is considered a breaking change, and will raise an error.

Remember that `state:modified` includes *all* of the criteria above, as well as some extra resource-specific criteria, such as modifying a source's `freshness` or `quoting` rules or an exposure's `maturity` property. (View the source code for the full set of checks used when comparing [sources](https://github.com/dbt-labs/dbt-core/blob/9e796671dd55d4781284d36c035d1db19641cd80/core/dbt/contracts/graph/parsed.py#L660-L681), [exposures](https://github.com/dbt-labs/dbt-core/blob/9e796671dd55d4781284d36c035d1db19641cd80/core/dbt/contracts/graph/parsed.py#L768-L783), and [executable nodes](https://github.com/dbt-labs/dbt-core/blob/9e796671dd55d4781284d36c035d1db19641cd80/core/dbt/contracts/graph/parsed.py#L319-L330).)

There are two additional `state` selectors that complement `state:new` and `state:modified` by representing the inverse of those functions:

* `state:old` — A node with the same `unique_id` exists in the comparison manifest
* `state:unmodified` — All existing nodes with no changes

These selectors can help you shorten run times by excluding unchanged nodes. Currently, no subselectors are available at this time, but that might change as use cases evolve.

#### `state:modified` node and reference impacts[​](#statemodified-node-and-reference-impacts "Direct link to statemodified-node-and-reference-impacts")

`state:modified` identifies any new nodes added, changes to existing nodes, and any changes made to:

* [access](/reference/resource-configs/access) permissions
* [`deprecation_date`](/reference/resource-properties/deprecation_date)
* [`latest_version`](/reference/resource-properties/latest_version)

If a node changes its group, downstream references may break, potentially causing build failures.

As `group` is a config, and configs are generally included in `state:modified` detection, modifying the group name everywhere it's referenced will flag those nodes as "modified".

Depending on whether partial parsing is enabled, you will catch the breakage as part of CI workflows.

* If you change a group name everywhere it's referenced, and partial parsing is enabled, dbt may only re-parse the changed model.
* If you update a group name in all its references without partial parsing enabled, dbt will re-parse all models and identify any invalid downstream references.

An error along the lines of "there's nothing to do" can occur when you change the group name *and* something is picked up to be run via `dbt build --select state:modified`. This error will be caught at runtime so long as the CI job is selecting `state:modified+` (including downstreams).

Certain factors can affect how references are used or resolved later on, including:

* Modifying access: if permissions or access rules change, some references might stop working.
* Modifying `deprecation_date`: if a reference or model version is marked deprecated, new warnings might appear that affect how references are processed.
* Modifying `latest_version`: if there's no tie to a specific version, the reference or model will point to the latest version.
  + If a newer version is released, the reference will automatically resolve to the new version, potentially changing the behavior or output of the system that relies on it.

#### Overwrites the `manifest.json`[​](#overwrites-the-manifestjson "Direct link to overwrites-the-manifestjson")

dbt overwrites the `manifest.json` file during parsing, which means when you reference `--state` from the `target/ directory`, you may encounter a warning indicating that the saved manifest wasn't found.

[![Saved manifest not found error](/img/docs/reference/saved-manifest-not-found.png?v=2 "Saved manifest not found error")](#)Saved manifest not found error

During the next job run, dbt follows a sequence of steps that lead to the issue. First, it overwrites `target/manifest.json` before it can be used for change detection. Then, when dbt tries to read `target/manifest.json` again to detect changes, it finds none because the previous state has already been overwritten/erased.

Avoid setting `--state` and `--target-path` to the same path with state-dependent features like `--defer` and `state:modified` as it can lead to non-idempotent behavior and won't work as expected.

#### Recommendation[​](#recommendation "Direct link to Recommendation")

To prevent the `manifest.json` from being overwritten before dbt reads it for change detection, update your workflow using one of these methods:

* Move the `manifest.json` to a dedicated folder (for example `state/`) after dbt generates it in the `target/ folder`. This makes sure dbt references the correct saved state instead of comparing the current state with the just-overwritten version. It also avoids issues caused by setting `--state` and `--target-path` to the same location, which can lead to non-idempotent behavior.
* Write the manifest to a different `--target-path` in the build stage (where dbt would generate the `target/manifest.json`) or before it gets overwritten during job execution to avoid issues with change detection. This allows dbt to detect changes instead of comparing the current state with the just-overwritten version.
* Pass the `--no-write-json` flag: `dbt ls --no-write-json --select state:modified --state target`: during the reproduction stage.

### tag[​](#tag "Direct link to tag")

The `tag:` method is used to select models that match a specified [tag](/reference/resource-configs/tags).

```
dbt run --select "tag:nightly"    # run all models with the `nightly` tag
```

### test\_name[​](#test_name "Direct link to test_name")

The `test_name` method is used to select tests based on the name of the generic test
that defines it. For more information about how generic tests are defined, read about
[data tests](/docs/build/data-tests).

```
dbt test --select "test_name:unique"            # run all instances of the `unique` test  
dbt test --select "test_name:equality"          # run all instances of the `dbt_utils.equality` test  
dbt test --select "test_name:range_min_max"     # run all instances of a custom schema test defined in the local project, `range_min_max`
```

### The test\_type[​](#the-test_type "Direct link to The test_type")

The `test_type` method is used to select tests based on their type:

* [Unit tests](/docs/build/unit-tests)
* [Data tests](/docs/build/data-tests):
  + [Singular](/docs/build/data-tests#singular-data-tests)
  + [Generic](/docs/build/data-tests#generic-data-tests)

```
dbt test --select "test_type:unit"           # run all unit tests  
dbt test --select "test_type:data"           # run all data tests  
dbt test --select "test_type:generic"        # run all generic data tests  
dbt test --select "test_type:singular"       # run all singular data tests
```

### unit\_test[​](#unit_test "Direct link to unit_test")

The `unit_test` method selects [unit tests](/docs/build/unit-tests).

```
dbt list --select "unit_test:*"                        # list all unit tests   
dbt list --select "+unit_test:orders_with_zero_items"  # list your unit test named "orders_with_zero_items" and all upstream resources
```

### version[​](#version "Direct link to version")

The `version` method selects [versioned models](/docs/mesh/govern/model-versions) based on their [version identifier](/reference/resource-properties/versions) and [latest version](/reference/resource-properties/latest_version).

```
dbt list --select "version:latest"      # only 'latest' versions  
dbt list --select "version:prerelease"  # versions newer than the 'latest' version  
dbt list --select "version:old"         # versions older than the 'latest' version  
  
dbt list --select "version:none"        # models that are *not* versioned
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/node-selection/methods.md)

Last updated on **Nov 19, 2025**

[Previous

Set operators](/reference/node-selection/set-operators)[Next

Putting it together](/reference/node-selection/putting-it-together)

* [access](#access)
* [config](#config)
* [exposure](#exposure)
* [file](#file)
* [fqn](#fqn)
* [group](#group)
* [metric](#metric)
* [package](#package)
* [path](#path)
* [resource\_type](#resource_type)
* [result](#result)
* [saved\_query](#saved_query)
* [semantic\_model](#semantic_model)
* [source](#source)
* [source\_status](#source_status)
* [state](#state)
* [tag](#tag)
* [test\_name](#test_name)
* [The test\_type](#the-test_type)
* [unit\_test](#unit_test)
* [version](#version)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/node-selection/methods.md)

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