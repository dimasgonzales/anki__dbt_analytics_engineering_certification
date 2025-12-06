# Source: https://docs.getdbt.com/docs/cloud/manage-access/environment-permissions

About environment-level permissions | dbt Developer Hub

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

  + [About dbt setup](/docs/about-setup)
  + [About environments](/docs/environments-in-dbt)
  + [dbt platform](/docs/cloud/about-cloud-setup)

    - [About dbt setup](/docs/cloud/about-cloud-setup)
    - [Account settings](/docs/cloud/account-settings)
    - [Account integrations](/docs/cloud/account-integrations)
    - [dbt environments](/docs/dbt-cloud-environments)
    - [Multi-cell migration checklist](/docs/cloud/migration)
    - [Connect your data platforms](/docs/cloud/connect-data-platform/about-connections)
    - [Manage access](/docs/cloud/manage-access/about-user-access)

      * [About user access in dbt](/docs/cloud/manage-access/about-user-access)
      * [Invite users to dbt](/docs/cloud/manage-access/invite-users)
      * [Multi-factor authentication](/docs/cloud/manage-access/mfa)
      * [User permissions and licenses](/docs/cloud/manage-access/seats-and-users)
      * [Environment permissions](/docs/cloud/manage-access/environment-permissions)

        + [Environment-level permissions](/docs/cloud/manage-access/environment-permissions)
        + [Set up environment-level permissions](/docs/cloud/manage-access/environment-permissions-setup)
      * [Single sign-on and Oauth](/docs/cloud/manage-access/sso-overview)
      * [Audit log](/docs/cloud/manage-access/audit-log)
    - [Configure Git](/docs/cloud/git/git-configuration-in-dbt-cloud)
    - [Secure your tenant](/docs/cloud/secure/secure-your-tenant)
  + [dbt Core and Fusion](/docs/about-dbt-install)
  + [Run your dbt projects](/docs/running-a-dbt-project/run-your-dbt-projects)
  + [Use threads](/docs/running-a-dbt-project/using-threads)
* Build and develop
* [Develop with dbt](/docs/cloud/about-develop-dbt)
* [Build dbt projects](/docs/build/projects)
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

* [Set up dbt](/docs/about-setup)
* [dbt platform](/docs/cloud/about-cloud-setup)
* [Manage access](/docs/cloud/manage-access/about-user-access)
* Environment permissions

Copy page

On this page

About environment-level permissions
===================================

Environment-level permissions give dbt admins the ability to grant write permission to groups and service tokens for specific [environment types](/docs/dbt-cloud-environments) within a project. Granting access to an environment give users access to all environment-level write actions and resources associated with their assigned roles. For example, users with a Developer role can create and run jobs within the environment(s) they have access to. For all other environments, those same users will have read-only access.

For configuration instructions, check out the [setup page](/docs/cloud/manage-access/environment-permissions-setup).

Current limitations[​](#current-limitations "Direct link to Current limitations")
---------------------------------------------------------------------------------

Environment-level permissions give dbt admins more flexibility to protect their environments, but it's important to understand that there are some limitations to this feature, so those admins can make informed decisions about granting access.

* Environment-level permissions do not allow you to create custom roles and permissions for each resource type in dbt.
* You can only select environment types, and can’t specify a particular environment within a project.
* You can't select specific resources within environments. dbt jobs and runs are environment resources.
  + For example, you can't specify that a user only has access to jobs but not runs. Access to a given environment gives the user access to everything within that environment.

Environments and roles[​](#environments-and-roles "Direct link to Environments and roles")
------------------------------------------------------------------------------------------

dbt has four different environment types per project:

* **Production** — Primary deployment environment. Only one unique Production env per project.
* **Development** — Developer testing environment. Only one unique Development env per project.
* **Staging** — Pre-prod environment that sits between development and production. Only one unique Staging env per project.
* **General** — Mixed use environments. No limit on the number per project.

Environment write permissions can be specified for the following roles:

* Analyst
* Database admin
* Developer (Previous default write access for all environments. The new default is read access for environments unless access is specified)
* Git admin
* Team admin

Depending on your current group mappings, you may have to update roles to ensure users have the correct access level to environments.

Determine what personas need updated environment access and the roles they should be mapped to. The personas below highlight a few scenarios for environment permissions:

* **Developer** — Write access to create/run jobs in non-production environments
* **Testing/QA** — Write access to staging and development environments to test
* **Production deployment** — Write access to all environments, including production, for deploying
* **Analyst** — Doesn't need environmental write access but read-only access for discovery and troubleshooting
* **Other admins** — These admins may need write access to create/run jobs or configure integrations for any number of environments

Projects and environments[​](#projects-and-environments "Direct link to Projects and environments")
---------------------------------------------------------------------------------------------------

Environment-level permissions can be enforced over one or multiple projects with mixed access to the environments themselves.

### Single project environments[​](#single-project-environments "Direct link to Single project environments")

If you’re working with a single project, we recommend restricting access to the Production environment and ensuring groups have access to Development, Staging, or General environments where they can safely create and run jobs. The following is an example of how the personas could be mapped to roles:

* **Developer:** Developer role with write access to Development and General environments
* **Testing/QA:** Developer role with write access to Development, Staging, and General environments
* **Production Deployment:** Developer role with write access to all environments or Job Admin which has access to all environments by default.
* **Analyst:** Analyst role with no write access and read-only access to environments.
* **Other Admins:** Depends on the admin needs. For example, if they are managing the production deployment grant access to all environments.

### Multiple projects[​](#multiple-projects "Direct link to Multiple projects")

Let's say Acme corp has 12 projects and 3 of them belong to Finance, 3 belong to Marketing, 4 belong to Manufacturing, and 2 belong to Technology.

With mixed access across projects:

* **Developer:** If the user has the Developer role and has access to Projects A, B, C, then they only need access to Dev and General environments.
* **Testing/QA:** If they have the Developer role and they have access to Projects A, B, C, then they only need access to Development, Staging, and General environments.
* **Production Deployment:** If the user has the Admin *or* Developer role *and* they have access to Projects A, B, C, then they need access to all Environments.
* **Analyst:** If the user has the Analyst role, then the need *no* write access to *any environment*.
* **Other Admins:** A user (non-Admin) can have access to multiple projects depending on the requirements.

If the user has the same roles across projects, you can apply environment access across all projects.

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [Environment-level permissions setup](/docs/cloud/manage-access/environment-permissions-setup)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/cloud/manage-access/environment-permissions.md)

Last updated on **Nov 19, 2025**

* [Current limitations](#current-limitations)
* [Environments and roles](#environments-and-roles)
* [Projects and environments](#projects-and-environments)
  + [Single project environments](#single-project-environments)
  + [Multiple projects](#multiple-projects)
* [Related docs](#related-docs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/cloud/manage-access/environment-permissions.md)

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