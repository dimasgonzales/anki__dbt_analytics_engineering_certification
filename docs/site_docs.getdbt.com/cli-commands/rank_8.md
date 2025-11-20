# Source: https://docs.getdbt.com/reference/programmatic-invocations

Programmatic invocations | dbt Developer Hub

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
* Programmatic invocations

Copy page

On this page

Programmatic invocations
========================

In v1.5, dbt Core added support for programmatic invocations. The intent is to expose the existing dbt Core CLI via a Python entry point, such that top-level commands are callable from within a Python script or application.

The entry point is a `dbtRunner` class, which allows you to `invoke` the same commands as on the CLI.

```
from dbt.cli.main import dbtRunner, dbtRunnerResult  
  
# initialize  
dbt = dbtRunner()  
  
# create CLI args as a list of strings  
cli_args = ["run", "--select", "tag:my_tag"]  
  
# run the command  
res: dbtRunnerResult = dbt.invoke(cli_args)  
  
# inspect the results  
for r in res.result:  
    print(f"{r.node.name}: {r.status}")
```

Parallel execution not supported[​](#parallel-execution-not-supported "Direct link to Parallel execution not supported")
------------------------------------------------------------------------------------------------------------------------

[`dbt-core`](https://pypi.org/project/dbt-core/) doesn't support [safe parallel execution](/reference/dbt-commands#parallel-execution) for multiple invocations in the same process. This means it's not safe to run multiple dbt commands concurrently. It's officially discouraged and requires a wrapping process to handle sub-processes. This is because:

* Running concurrent commands can unexpectedly interact with the data platform. For example, running `dbt run` and `dbt build` for the same models simultaneously could lead to unpredictable results.
* Each `dbt-core` command interacts with global Python variables. To ensure safe operation, commands need to be executed in separate processes, which can be achieved using methods like spawning processes or using tools like Celery.

To run [safe parallel execution](/reference/dbt-commands#available-commands), you can use the [dbt CLI](/docs/cloud/cloud-cli-installation) or [Studio IDE](/docs/cloud/dbt-cloud-ide/develop-in-the-cloud), both of which does that additional work to manage concurrency (multiple processes) on your behalf.

`dbtRunnerResult`[​](#dbtrunnerresult "Direct link to dbtrunnerresult")
-----------------------------------------------------------------------

Each command returns a `dbtRunnerResult` object, which has three attributes:

* `success` (bool): Whether the command succeeded.
* `result`: If the command completed (successfully or with handled errors), its result(s). Return type varies by command.
* `exception`: If the dbt invocation encountered an unhandled error and did not complete, the exception it encountered.

There is a 1:1 correspondence between [CLI exit codes](/reference/exit-codes) and the `dbtRunnerResult` returned by a programmatic invocation:

| Scenario | CLI Exit Code | `success` | `result` | `exception` |
| --- | --- | --- | --- | --- |
| Invocation completed without error | 0 | `True` | varies by command | `None` |
| Invocation completed with at least one handled error (e.g. test failure, model build error) | 1 | `False` | varies by command | `None` |
| Unhandled error. Invocation did not complete, and returns no results. | 2 | `False` | `None` | Exception |

Commitments & Caveats[​](#commitments--caveats "Direct link to Commitments & Caveats")
--------------------------------------------------------------------------------------

From dbt Core v1.5 onward, we making an ongoing commitment to providing a Python entry point at functional parity with dbt Core's CLI. We reserve the right to change the underlying implementation used to achieve that goal. We expect that the current implementation will unlock real use cases, in the short & medium term, while we work on a set of stable, long-term interfaces that will ultimately replace it.

In particular, the objects returned by each command in `dbtRunnerResult.result` are not fully contracted, and therefore liable to change. Some of the returned objects are partially documented, because they overlap in part with the contents of [dbt artifacts](/reference/artifacts/dbt-artifacts). As Python objects, they contain many more fields and methods than what's available in the serialized JSON artifacts. These additional fields and methods should be considered **internal and liable to change in future versions of dbt-core.**

Advanced usage patterns[​](#advanced-usage-patterns "Direct link to Advanced usage patterns")
---------------------------------------------------------------------------------------------

caution

The syntax and support for these patterns are liable to change in future versions of `dbt-core`.

The goal of `dbtRunner` is to offer parity with CLI workflows, within a programmatic environment. There are a few advanced usage patterns that extend what's possible with the CLI.

### Reusing objects[​](#reusing-objects "Direct link to Reusing objects")

Pass pre-constructed objects into `dbtRunner`, to avoid recreating those objects by reading files from disk. Currently, the only object supported is the `Manifest` (project contents).

```
from dbt.cli.main import dbtRunner, dbtRunnerResult  
from dbt.contracts.graph.manifest import Manifest  
  
# use 'parse' command to load a Manifest  
res: dbtRunnerResult = dbtRunner().invoke(["parse"])  
manifest: Manifest = res.result  
  
# introspect manifest  
# e.g. assert every public model has a description  
for node in manifest.nodes.values():  
    if node.resource_type == "model" and node.access == "public":  
        assert node.description != "", f"{node.name} is missing a description"  
  
# reuse this manifest in subsequent commands to skip parsing  
dbt = dbtRunner(manifest=manifest)  
cli_args = ["run", "--select", "tag:my_tag"]  
res = dbt.invoke(cli_args)
```

### Registering callbacks[​](#registering-callbacks "Direct link to Registering callbacks")

Register `callbacks` on dbt's `EventManager`, to access structured events and enable custom logging. The current behavior of callbacks is to block subsequent steps from proceeding; this functionality is not guaranteed in future versions.

```
from dbt.cli.main import dbtRunner  
from dbt_common.events.base_types import EventMsg  
  
def print_version_callback(event: EventMsg):  
    if event.info.name == "MainReportVersion":  
        print(f"We are thrilled to be running dbt{event.data.version}")  
  
dbt = dbtRunner(callbacks=[print_version_callback])  
dbt.invoke(["list"])
```

### Overriding parameters[​](#overriding-parameters "Direct link to Overriding parameters")

Pass in parameters as keyword arguments, instead of a list of CLI-style strings. At present, dbt will not do any validation or type coercion on your inputs. The subcommand must be specified, in a list, as the first positional argument.

```
from dbt.cli.main import dbtRunner  
dbt = dbtRunner()  
  
# these are equivalent  
dbt.invoke(["--fail-fast", "run", "--select", "tag:my_tag"])  
dbt.invoke(["run"], select=["tag:my_tag"], fail_fast=True)
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/programmatic-invocations.md)

Last updated on **Nov 19, 2025**

[Previous

Project Parsing](/reference/parsing)[Next

Jinja reference](/category/jinja-reference)

* [Parallel execution not supported](#parallel-execution-not-supported)
* [`dbtRunnerResult`](#dbtrunnerresult)
* [Commitments & Caveats](#commitments--caveats)
* [Advanced usage patterns](#advanced-usage-patterns)
  + [Reusing objects](#reusing-objects)
  + [Registering callbacks](#registering-callbacks)
  + [Overriding parameters](#overriding-parameters)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/programmatic-invocations.md)

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