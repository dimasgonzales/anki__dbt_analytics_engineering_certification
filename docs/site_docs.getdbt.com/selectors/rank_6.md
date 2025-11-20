# Source: https://docs.getdbt.com/reference/node-selection/yaml-selectors

YAML Selectors | dbt Developer Hub

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
* YAML Selectors

Copy page

On this page

YAML Selectors
==============

Write resource selectors in YAML, save them with a human-friendly name, and reference them using the `--selector` flag.
By recording selectors in a top-level `selectors.yml` file:

* **Legibility:** complex selection criteria are composed of dictionaries and arrays
* **Version control:** selector definitions are stored in the same git repository as the dbt project
* **Reusability:** selectors can be referenced in multiple job definitions, and their definitions are extensible (via YAML anchors)

Selectors live in a top-level file named `selectors.yml`. Each must have a `name` and a `definition`, and can optionally define a `description` and [`default` flag](#default).

selectors.yml

```
selectors:  
  - name: nodes_to_joy  
    definition: ...  
  - name: nodes_to_a_grecian_urn  
    description: Attic shape with a fair attitude  
    default: true  
    definition: ...
```

Definitions[​](#definitions "Direct link to Definitions")
---------------------------------------------------------

Each `definition` is comprised of one or more arguments, which can be one of the following:

* **CLI-style:** strings, representing CLI-style arguments
* **Key-value:** pairs in the form `method: value`
* **Full YAML:** fully specified dictionaries with items for `method`, `value`, operator-equivalent keywords, and support for `exclude`

Use the `union` and `intersection` operator-equivalent keywords to organize multiple arguments.

### CLI-style[​](#cli-style "Direct link to CLI-style")

```
definition:  
  'tag:nightly'
```

This simple syntax supports use of the `+`, `@`, and `*` [graph](/reference/node-selection/graph-operators) operators, [set](/reference/node-selection/set-operators) operators, and `exclude`.

### Key-value[​](#key-value "Direct link to Key-value")

```
definition:  
  tag: nightly
```

This simple syntax does not support any [graph](/reference/node-selection/graph-operators) or [set](/reference/node-selection/set-operators) operators or `exclude`.

### Full YAML[​](#full-yaml "Direct link to Full YAML")

This is the most thorough syntax, which can include the operator-equivalent keywords for [graph](/reference/node-selection/graph-operators) and [set](/reference/node-selection/set-operators) operators.

Review [methods](/reference/node-selection/methods) for the available list.

```
definition:  
  method: tag  
  value: nightly  
  
  # Optional keywords map to the `+` and `@` graph operators:  
  
  children: true | false  
  parents: true | false  
  
  children_depth: 1    # if children: true, degrees to include  
  parents_depth: 1     # if parents: true, degrees to include  
  
  childrens_parents: true | false     # @ operator  
  
  indirect_selection: eager | cautious | buildable | empty # include all tests selected indirectly? eager by default
```

The `*` operator to select all nodes can be written as:

```
definition:  
  method: fqn  
  value: "*"
```

#### Exclude[​](#exclude "Direct link to Exclude")

The `exclude` keyword is only supported by fully-qualified dictionaries.
It may be passed as an argument to each dictionary, or as
an item in a `union`. The following are equivalent:

```
- method: tag  
  value: nightly  
  exclude:  
    - "@tag:daily"
```

```
- union:  
    - method: tag  
      value: nightly  
    - exclude:  
       - method: tag  
         value: daily
```

Note: The `exclude` argument in YAML selectors is subtly different from
the `--exclude` CLI argument. Here, `exclude` *always* returns a [set difference](https://en.wikipedia.org/wiki/Complement_(set_theory)),
and it is always applied *last* within its scope.

When more than one "yeslist" (`--select`) is passed, they are treated as a [union](/reference/node-selection/set-operators#unions) rather than an [intersection](/reference/node-selection/set-operators#intersections). Same thing when there is more than one "nolist" (`--exclude`).

#### Indirect selection[​](#indirect-selection "Direct link to Indirect selection")

As a general rule, dbt will indirectly select *all* tests if they touch *any* resource that you're selecting directly. We call this "eager" indirect selection. You can optionally switch the indirect selection mode to "cautious", "buildable", or "empty" by setting `indirect_selection` for a specific criterion:

```
- union:  
    - method: fqn  
      value: model_a  
      indirect_selection: eager  # default: will include all tests that touch model_a  
    - method: fqn  
      value: model_b  
      indirect_selection: cautious  # will not include tests touching model_b  
                        # if they have other unselected parents  
    - method: fqn  
      value: model_c  
      indirect_selection: buildable  # will not include tests touching model_c  
                        # if they have other unselected parents (unless they have an ancestor that is selected)  
    - method: fqn  
      value: model_d  
      indirect_selection: empty  # will include tests for only the selected node and ignore all tests attached to model_d
```

If provided, a YAML selector's `indirect_selection` value will take precedence over the CLI flag `--indirect-selection`. Because `indirect_selection` is defined separately for *each* selection criterion, it's possible to mix eager/cautious/buildable/empty modes within the same definition, to achieve the exact behavior that you need. Remember that you can always test out your critiera with `dbt ls --selector`.

See [test selection examples](/reference/node-selection/test-selection-examples) for more details about indirect selection.

Example[​](#example "Direct link to Example")
---------------------------------------------

Here are two ways to represent:

```
$ dbt run --select @source:snowplow,tag:nightly models/export --exclude package:snowplow,config.materialized:incremental export_performance_timing
```

* CLI-style
* Full YML

selectors.yml

```
selectors:  
  - name: nightly_diet_snowplow  
    description: "Non-incremental Snowplow models that power nightly exports"  
    definition:  
  
      # Optional `union` and `intersection` keywords map to the ` ` and `,` set operators:  
      union:  
        - intersection:  
            - '@source:snowplow'  
            - 'tag:nightly'  
        - 'models/export'  
        - exclude:  
            - intersection:  
                - 'package:snowplow'  
                - 'config.materialized:incremental'  
            - export_performance_timing
```

selectors.yml

```
selectors:  
  - name: nightly_diet_snowplow  
    description: "Non-incremental Snowplow models that power nightly exports"  
    definition:  
      # Optional `union` and `intersection` keywords map to the ` ` and `,` set operators:  
      union:  
        - intersection:  
            - method: source  
              value: snowplow  
              childrens_parents: true  
            - method: tag  
              value: nightly  
        - method: path  
          value: models/export  
        - exclude:  
            - intersection:  
                - method: package  
                  value: snowplow  
                - method: config.materialized  
                  value: incremental  
            - method: fqn  
              value: export_performance_timing
```

Then in our job definition:

```
dbt run --selector nightly_diet_snowplow
```

Default[​](#default "Direct link to Default")
---------------------------------------------

Selectors may define a boolean `default` property. If a selector has `default: true`, dbt will use this selector's criteria when tasks do not define their own selection criteria.

Let's say we define a default selector that only selects resources defined in our root project:

```
selectors:  
  - name: root_project_only  
    description: >  
        Only resources from the root project.  
        Excludes resources defined in installed packages.  
    default: true  
    definition:  
      method: package  
      value: <my_root_project_name>
```

If I run an "unqualified" command, dbt will use the selection criteria defined in `root_project_only`—that is, dbt will only build / freshness check / generate compiled SQL for resources defined in my root project.

```
dbt build  
dbt source freshness  
dbt docs generate
```

If I run a command that defines its own selection criteria (via `--select`, `--exclude`, or `--selector`), dbt will ignore the default selector and use the flag criteria instead. It will not try to combine the two.

```
dbt run --select  "model_a"  
dbt run --exclude model_a
```

Only one selector may set `default: true` for a given invocation; otherwise, dbt will return an error. You may use a Jinja expression to adjust the value of `default` depending on the environment, however:

```
selectors:  
  - name: default_for_dev  
    default: "{{ target.name == 'dev' | as_bool }}"  
    definition: ...  
  - name: default_for_prod  
    default: "{{ target.name == 'prod' | as_bool }}"  
    definition: ...
```

### Selector inheritance[​](#selector-inheritance "Direct link to Selector inheritance")

Selectors can reuse and extend definitions from other selectors, via the `selector` method.

```
selectors:  
  - name: foo_and_bar  
    definition:  
      intersection:  
        - tag: foo  
        - tag: bar  
  
  - name: foo_bar_less_buzz  
    definition:  
      intersection:  
        # reuse the definition from above  
        - method: selector  
          value: foo_and_bar  
        # with a modification!  
        - exclude:  
            - method: tag  
              value: buzz
```

**Note:** While selector inheritance allows the logic from another selector to be *reused*, it doesn't allow the logic from that selector to be *modified* by means of `parents`, `children`, `indirect_selection`, and so on.

The `selector` method returns the complete set of nodes returned by the named selector.

Difference between `--select` and `--selector`[​](#difference-between---select-and---selector "Direct link to difference-between---select-and---selector")
----------------------------------------------------------------------------------------------------------------------------------------------------------

In dbt, [`select`](/reference/node-selection/syntax#how-does-selection-work) and `selector` are related concepts used for choosing specific models, tests, or resources. The following tables explains the differences and when to best use them:

| Feature | `--select` | `--selector` |
| --- | --- | --- |
| Definition | Ad-hoc, specified directly in the command. | Pre-defined in `selectors.yml` file. |
| Usage | One-time or task-specific filtering. | Reusable for multiple executions. |
| Complexity | Requires manual entry of selection criteria. | Can encapsulate complex logic for reuse. |
| Flexibility | Flexible; less reusable. | Flexible; focuses on reusable and structured logic. |
| Example | `dbt run --select my_model+`  (runs `my_model` and all downstream dependencies with the `+` operator). | `dbt run --selector nightly_diet_snowplow`  (runs models defined by the `nightly_diet_snowplow` selector in `selectors.yml`). |

Notes:

* You can combine `--select` with `--exclude` for ad-hoc selection of nodes.
* The `--select` and `--selector` syntax both provide the same overall functions for node selection. Using [graph operators](/reference/node-selection/graph-operators) (such as `+`, `@`.) and [set operators](/reference/node-selection/set-operators) (such as `union` and `intersection`) in `--select` is the same as YAML-based configs in `--selector`.

For additional examples, check out [this GitHub Gist](https://gist.github.com/jeremyyeo/1aeca767e2a4f157b07955d58f8078f7).

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/node-selection/yaml-selectors.md)

Last updated on **Nov 19, 2025**

[Previous

Putting it together](/reference/node-selection/putting-it-together)[Next

Test selection examples](/reference/node-selection/test-selection-examples)

* [Definitions](#definitions)
  + [CLI-style](#cli-style)
  + [Key-value](#key-value)
  + [Full YAML](#full-yaml)
* [Example](#example)
* [Default](#default)
  + [Selector inheritance](#selector-inheritance)
* [Difference between `--select` and `--selector`](#difference-between---select-and---selector)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/node-selection/yaml-selectors.md)

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