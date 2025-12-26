I'm getting a "Session occupied" error in dbt CLI? | dbt Developer Hub

[Skip to main content](#__docusaurus_skipToContent_fallback)

[Join our virtual event on Dec 16 & 17: Delivering reliable AI with the dbt Semantic Layer and dbt MCP Server](https://www.getdbt.com/resources/webinars/delivering-reliable-ai-with-the-dbt-semantic-layer-and-dbt-mcp-server)

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

* [Frequently asked questions](/docs/faqs)

  + [Accounts](/category/accounts)
  + [dbt Core](/category/dbt-core)
  + [Documentation](/category/documentation)
  + [Environments](/category/environments)
  + [Git](/category/git)
  + [Jinja](/category/jinja)
  + [Models](/category/models)
  + [Projects](/category/projects)
  + [Project\_ref](/faqs/Project_ref/define-private-packages)
  + [Runs](/category/runs)
  + [Seeds](/category/seeds)
  + [Snapshots](/category/snapshots)
  + [Tests](/category/tests)
  + [Troubleshooting](/category/troubleshooting)

    - [Generate HAR files](/faqs/Troubleshooting/generate-har-file)
    - [Error when trying to query from Google Drive](/faqs/Troubleshooting/access-gdrive-credential)
    - [Receiving `authentication has expired` error in the IDE](/faqs/Troubleshooting/auth-expired-error)
    - [Could not parse dbt\_project.yml error in dbt](/faqs/Troubleshooting/could-not-parse-project)
    - [Could not find package error](/faqs/Troubleshooting/dispatch-could-not-find-package)
    - [Errors importing a repository on dbt project set up](/faqs/Troubleshooting/error-importing-repo)
    - [Receiving `Failed to connect to database` error](/faqs/Troubleshooting/failed-snowflake-oauth-connection)
    - [Receiving git rev-list master error in the IDE](/faqs/Troubleshooting/git-revlist-error)
    - [How to fix your .gitignore file](/faqs/Troubleshooting/gitignore)
    - [GitLab authentication out of date](/faqs/Troubleshooting/gitlab-authentication)
    - [Unable to trigger a CI job](/faqs/Troubleshooting/gitlab-webhook)
    - [Receiving unknown error in the IDE](/faqs/Troubleshooting/ide-session-unknown-error)
    - [Service token 403 error: Forbidden: Access denied](/faqs/Troubleshooting/ip-restrictions)
    - [Job failures due to exceeded memory limits](/faqs/Troubleshooting/job-memory-limits)
    - [Debug long-running sessions in dbt CLI](/faqs/Troubleshooting/long-sessions-cloud-cli)
    - [NoneType error in the IDE](/faqs/Troubleshooting/nonetype-ide-error)
    - [Partial\_parse error in the IDE](/faqs/Troubleshooting/partial-parsing-error)
    - [Could not find profile named user"error in the IDE](/faqs/Troubleshooting/runtime-error-could-not-find-profile)
    - [Runtime error in packages.yml file](/faqs/Troubleshooting/runtime-packages.yml)
    - [Use SSL exception to resolve `Failed ALPN` error](/faqs/Troubleshooting/sl-alpn-error)
    - [How to debug SQL or database error](/faqs/Troubleshooting/sql-errors)
    - [Receiving an unused model configurations error](/faqs/Troubleshooting/unused-model-configurations)
  + [Warehouse](/category/warehouse)

* [Frequently asked questions](/docs/faqs)
* [Troubleshooting](/category/troubleshooting)
* Debug long-running sessions in dbt CLI

Copy page

Copy page

Copy page as Markdown for LLMs

[Open in ChatGPT

Ask questions about this page](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Ffaqs%2FTroubleshooting%2Flong-sessions-cloud-cli+so+I+can+ask+questions+about+it.)[Open in Claude

Ask questions about this page](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Ffaqs%2FTroubleshooting%2Flong-sessions-cloud-cli+so+I+can+ask+questions+about+it.)[Open in Perplexity

Ask questions about this page](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Ffaqs%2FTroubleshooting%2Flong-sessions-cloud-cli+so+I+can+ask+questions+about+it.)

I'm getting a "Session occupied" error in dbt CLI?
==================================================

If you're receiving a `Session occupied` error in the Cloud CLI or if you're experiencing a long-running session, you can use the `dbt invocation list` command in a separate terminal window to view the status of your active session. This helps debug the issue and identify the arguments that are causing the long-running session.

To cancel an active session, use the `Ctrl + Z` shortcut.

To learn more about the `dbt invocation` command, see the [dbt invocation command reference](/reference/commands/invocation).

Alternatively, you can reattach to your existing session with `dbt reattach` and then press `Control-C` and choose to cancel the invocation.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/faqs/Troubleshooting/long-sessions-cloud-cli.md)

Last updated on **Dec 4, 2025**

[Previous

Job failures due to exceeded memory limits](/faqs/Troubleshooting/job-memory-limits)[Next

NoneType error in the IDE](/faqs/Troubleshooting/nonetype-ide-error)

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