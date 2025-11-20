# Source: https://docs.getdbt.com/category/list-of-commands

List of commands | dbt Developer Hub

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

    - [build](/reference/commands/build)
    - [clean](/reference/commands/clean)
    - [clone](/reference/commands/clone)
    - [docs](/reference/commands/cmd-docs)
    - [compile](/reference/commands/compile)
    - [debug](/reference/commands/debug)
    - [deps](/reference/commands/deps)
    - [environment](/reference/commands/dbt-environment)
    - [init](/reference/commands/init)
    - [invocation](/reference/commands/invocation)
    - [ls (list)](/reference/commands/list)
    - [parse](/reference/commands/parse)
    - [retry](/reference/commands/retry)
    - [rpc](/reference/commands/rpc)
    - [run](/reference/commands/run)
    - [run-operation](/reference/commands/run-operation)
    - [seed](/reference/commands/seed)
    - [show](/reference/commands/show)
    - [snapshot](/reference/commands/snapshot)
    - [source](/reference/commands/source)
    - [test](/reference/commands/test)
    - [version](/reference/commands/version)
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
* List of commands

List of commands
================

The list of commands available in dbt.

[📄️ build
--------

The dbt build command will:](/reference/commands/build)

[📄️ clean
--------

dbt clean is a utility function that deletes the paths specified within the clean-targets list in the dbt\_project.yml file. It helps by removing unnecessary files or directories generated during the execution of other dbt commands, ensuring a clean state for the project.](/reference/commands/clean)

[📄️ clone
--------

The dbt clone command clones selected nodes from the specified state to the target schema(s). This command makes use of the clone materialization:](/reference/commands/clone)

[📄️ docs
-------

Generate and serve the docs for your dbt project.](/reference/commands/cmd-docs)

[📄️ compile
----------

The dbt compile command creates executable SQL from model, test, and analysis files.](/reference/commands/compile)

[📄️ debug
--------

Use dbt debug to test database connections and check system setup.](/reference/commands/debug)

[📄️ deps
-------

dbt deps pulls the most recent version of the dependencies listed in your packages.yml from git. See Package-Management for more information.](/reference/commands/deps)

[📄️ environment
--------------

The dbt environment command enables you to interact with your environment. Use the command for:](/reference/commands/dbt-environment)

[📄️ init
-------

dbt init helps get you started using !](/reference/commands/init)

[📄️ invocation
-------------

The dbt invocation command is available in the and allows you to:](/reference/commands/invocation)

[📄️ ls (list)
------------

Read this guide on how dbt's ls (list) command can be used to list resources in your dbt project.](/reference/commands/list)

[📄️ parse
--------

Read this guide on how dbt's parse command can be used to parse your dbt project and write detailed timing information.](/reference/commands/parse)

[📄️ retry
--------

dbt retry re-executes the last dbt command from the node point of failure.](/reference/commands/retry)

[📄️ rpc
------

Remote Procedure Call (rpc) dbt server compiles and runs queries, and provides methods that enable you to list and terminate running processes.](/reference/commands/rpc)

[📄️ run
------

The dbt run command executes your compiled SQL models against a target database.](/reference/commands/run)

[📄️ run-operation
----------------

Read this guide on how dbt's run-operation command can be used to invoke a macro.](/reference/commands/run-operation)

[📄️ seed
-------

The dbt seed command will load csv files located in the seed-paths directory of your dbt project into your .](/reference/commands/seed)

[📄️ show
-------

Use dbt show to:](/reference/commands/show)

[📄️ snapshot
-----------

The dbt snapshot command executes the Snapshots defined in your project.](/reference/commands/snapshot)

[📄️ source
---------

The dbt source command provides subcommands that are useful when working with source data. This command provides one subcommand, dbt source freshness.](/reference/commands/source)

[📄️ test
-------

dbt test runs data tests defined on models, sources, snapshots, and seeds and unit tests defined on SQL models. It expects that you have already created those resources through the appropriate commands.](/reference/commands/test)

[📄️ version
----------

The --version command-line flag returns information about the currently installed version of or the . This flag is not supported when invoking dbt in other runtimes (for example, the IDE or scheduled runs).](/reference/commands/version)

[Previous

dbt Command reference](/reference/dbt-commands)[Next

build](/reference/commands/build)

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