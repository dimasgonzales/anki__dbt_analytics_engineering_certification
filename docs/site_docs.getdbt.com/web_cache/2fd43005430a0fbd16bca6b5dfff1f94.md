# Source: https://docs.getdbt.com/reference/commands/deps

About dbt deps command | dbt Developer Hub

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
* [List of commands](/category/list-of-commands)
* deps

Copy page

On this page

About dbt deps command
======================

`dbt deps` pulls the most recent version of the dependencies listed in your `packages.yml` from git. See [Package-Management](/docs/build/packages) for more information.

Where relevant, dbt will display up to date and/or latest versions of packages that are listed on dbt Hub. Example below.

> This does NOT apply to packages that are installed via git/local

```
packages:  
  - package: dbt-labs/dbt_utils  
    version: 0.7.1  
  - package: brooklyn-data/dbt_artifacts  
    version: 1.2.0  
    install-prerelease: true  
  - package: dbt-labs/codegen  
    version: 0.4.0  
  - package: calogica/dbt_expectations  
    version: 0.4.1  
  - git: https://github.com/dbt-labs/dbt_audit_helper.git  
    revision: 0.4.0  
  - git: "https://github.com/dbt-labs/dbt_labs-experimental-features" # git URL  
    subdirectory: "materialized-views" # name of subdirectory containing `dbt_project.yml`  
    revision: 0.0.1  
  - package: dbt-labs/snowplow  
    version: 0.13.0
```

```
Installing dbt-labs/dbt_utils@0.7.1  
  Installed from version 0.7.1  
  Up to date!  
Installing brooklyn-data/dbt_artifacts@1.2.0  
  Installed from version 1.2.0  
Installing dbt-labs/codegen@0.4.0  
  Installed from version 0.4.0  
  Up to date!  
Installing calogica/dbt_expectations@0.4.1  
  Installed from version 0.4.1  
  Up to date!  
Installing https://github.com/dbt-labs/dbt_audit_helper.git@0.4.0  
  Installed from revision 0.4.0  
Installing https://github.com/dbt-labs/dbt_labs-experimental-features@0.0.1  
  Installed from revision 0.0.1  
   and subdirectory materialized-views  
Installing dbt-labs/snowplow@0.13.0  
  Installed from version 0.13.0  
  Updated version available: 0.13.1  
Installing calogica/dbt_date@0.4.0  
  Installed from version 0.4.0  
  Up to date!  
  
Updates available for packages: ['tailsdotcom/dbt_artifacts', 'dbt-labs/snowplow']  
Update your versions in packages.yml, then run dbt deps
```

Predictable package installs[​](#predictable-package-installs "Direct link to Predictable package installs")
------------------------------------------------------------------------------------------------------------

dbt generates a `package-lock.yml` file in the root of your project. This file records the exact resolved versions (including commit SHAs) of all packages defined in your `packages.yml` or `dependencies.yml` file. The `package-lock.yml` file ensures consistent and repeatable installs across all environments.

When you run `dbt deps`, dbt installs packages based on the versions locked in the `package-lock.yml`. This means that as long as your packages file hasn’t changed, the exact same dependency versions will be installed even if newer versions of those packages have been released. This consistency is important to maintain stability in development and production environments, and to prevent unexpected issues from new releases with potential bugs.

If the `packages.yml` file has changed (for example, a new package is added or a version range is updated), then `dbt deps` automatically resolves the new set of dependencies and updates the lock file accordingly. You can also manually trigger an upgrade by running `dbt deps --upgrade`.

To maintain consistency, commit the `package-lock.yml` file to version control. This guarantees consistency across all environments and for all developers.

### Managing `package-lock.yml`[​](#managing-package-lockyml "Direct link to managing-package-lockyml")

The `package-lock.yml` file should be committed to Git initially and updated only when you intend to change versions or uninstall a package. For example, run `dbt deps --upgrade` to get updated package versions or `dbt deps --lock` to update the lock file based on changes to the packages config without installing the packages.

To bypass using `package-lock.yml` entirely, you can add it to your project's `.gitignore`. However, this approach sacrifices the predictability of builds. If you choose this route, we strongly recommend adding version pins for third-party packages in your `packages` config.

### Detecting changes in `packages` config[​](#detecting-changes-in-packages-config "Direct link to detecting-changes-in-packages-config")

The `package-lock.yml` file includes a `sha1_hash` of your packages config. If you update `packages.yml`, dbt will detect the change and rerun dependency resolution during the next `dbt deps` command. To update the lock file without installing the new packages, use the `--lock` flag:

```
dbt deps --lock
```

### Forcing package updates[​](#forcing-package-updates "Direct link to Forcing package updates")

To update all packages, even if `packages.yml` hasn't changed, use the `--upgrade` flag:

```
dbt deps --upgrade
```

This is particularly useful for fetching the latest commits from the `main` branch of an internally maintained Git package.

warning

Forcing package upgrades may introduce build inconsistencies unless carefully managed.

### Adding specific packages[​](#adding-specific-packages "Direct link to Adding specific packages")

The `dbt deps` command can add or update package configurations directly, saving you from remembering exact syntax.

#### Hub packages (default)[​](#hub-packages-default "Direct link to Hub packages (default)")

Hub packages are the default package types and the easiest to install.

```
dbt deps --add-package dbt-labs/dbt_utils@1.0.0  
  
# with semantic version range  
dbt deps --add-package dbt-labs/snowplow@">=0.7.0,<0.8.0"
```

#### Non-Hub packages[​](#non-hub-packages "Direct link to Non-Hub packages")

Use the `--source` flag to specify the type of package to be installed:

```
# Git package  
dbt deps --add-package https://github.com/fivetran/dbt_amplitude@v0.3.0 --source git  
  
# Local package  
dbt deps --add-package /opt/dbt/redshift --source local
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/commands/deps.md)

Last updated on **Nov 19, 2025**

[Previous

debug](/reference/commands/debug)[Next

environment](/reference/commands/dbt-environment)

* [Predictable package installs](#predictable-package-installs)
  + [Managing `package-lock.yml`](#managing-package-lockyml)
  + [Detecting changes in `packages` config](#detecting-changes-in-packages-config)
  + [Forcing package updates](#forcing-package-updates)
  + [Adding specific packages](#adding-specific-packages)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/commands/deps.md)

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