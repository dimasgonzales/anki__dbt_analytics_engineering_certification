# Source: https://docs.getdbt.com/docs/cloud/manage-access/audit-log

The audit log for dbt Enterprise | dbt Developer Hub

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
* Audit log

Copy page

On this page

dbt audit log [Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")
======================================================================================================================================================================================

To review actions performed by people in your organization, dbt provides logs of audited user and system events in real time. The audit log appears as events happen and includes details such as who performed the action, what the action was, and when it was performed. You can use these details to troubleshoot access issues, perform security audits, or analyze specific events.

You must be an **Account Admin** or an **Account Viewer** to access the audit log and this feature is only available on Enterprise plans.

The dbt audit log stores all the events that occurred in your organization in real-time, including:

* For events within 90 days, the dbt audit log has a selectable date range that lists events triggered.
* For events beyond 90 days, **Account Admins** and **Account Viewers** can [export all events](#exporting-logs) by using **Export All**.

Note that the retention period for events in the audit log is at least 12 months.

Accessing the audit log[​](#accessing-the-audit-log "Direct link to Accessing the audit log")
---------------------------------------------------------------------------------------------

To access the audit log, click on your account name in the left-side menu and select **Account settings**. Click **Audit log** in the left sidebar.

Understanding the audit log[​](#understanding-the-audit-log "Direct link to Understanding the audit log")
---------------------------------------------------------------------------------------------------------

On the audit log page, you will see a list of various events and their associated event data. Each of these events show the following information in dbt:

* **Event name**: Action that was triggered
* **Agent**: User who triggered that action/event
* **Timestamp**: Local timestamp of when the event occurred

### Event details[​](#event-details "Direct link to Event details")

Click the event card to see the details about the activity that triggered the event. This view provides important details, including when it happened and what type of event was triggered. For example, if someone changes the settings for a job, you can use the event details to see which job was changed (type of event: `job_definition.Changed`), by whom (person who triggered the event: `actor`), and when (time it was triggered: `created_at_utc`). For types of events and their descriptions, see [Events in audit log](#audit-log-events).

The event details provide the key factors of an event:

| Name | Description |
| --- | --- |
| account\_id | Account ID of where the event occurred |
| actor | Actor that carried out the event - User or Service |
| actor\_id | Unique ID of the actor |
| actor\_ip | IP address of the actor |
| actor\_name | Identifying name of the actor |
| actor\_type | Whether the action was done by a user or an API request |
| created\_at | UTC timestamp of when the event occurred |
| event\_type | Unique key identifying the event |
| event\_context | This key will be different for each event and will match the event\_type. This data will include all the details about the object(s) that was changed. |
| id | Unique ID of the event |
| service | Service that carried out the action |
| source | Source of the event - dbt UI or API |

Audit log events[​](#audit-log-events "Direct link to Audit log events")
------------------------------------------------------------------------

The audit log supports various events for different objects in dbt. You will find events for authentication, environment, jobs, service tokens, groups, user, project, permissions, license, connection, repository, and credentials.

### Authentication[​](#authentication "Direct link to Authentication")

| Event Name | Event Type | Description |
| --- | --- | --- |
| Auth Provider Changed | auth\_provider.changed | Authentication provider settings changed |
| Credential Login Succeeded | login.password.succeeded | User successfully logged in with username and password |
| SSO Login Failed | login.sso.failed | User login via SSO failed |
| SSO Login Succeeded | login.sso.succeeded | User successfully logged in via SSO |

### Environment[​](#environment "Direct link to Environment")

| Event Name | Event Type | Description |
| --- | --- | --- |
| Environment Added | environment.added | New environment successfully created |
| Environment Changed | environment.changed | Environment settings changed |
| Environment Removed | environment.removed | Environment successfully removed |

### Jobs[​](#jobs "Direct link to Jobs")

| Event Name | Event Type | Description |
| --- | --- | --- |
| Job Added | job\_definition.added | New Job successfully created |
| Job Changed | job\_definition.changed | Job settings changed |
| Job Removed | job\_definition.removed | Job definition removed |

### Service Token[​](#service-token "Direct link to Service Token")

| Event Name | Event Type | Description |
| --- | --- | --- |
| Service Token Created | service\_token.created | New Service Token was successfully created |
| Service Token Revoked | service\_token.revoked | Service Token was revoked |

### Group[​](#group "Direct link to Group")

| Event Name | Event Type | Description |
| --- | --- | --- |
| Group Added | group.added | New Group successfully created |
| Group Changed | group.changed | Group settings changed |
| Group Removed | group.removed | Group successfully removed |

### User[​](#user "Direct link to User")

| Event Name | Event Type | Description |
| --- | --- | --- |
| Invite Added | user.invite.added | User invitation added and sent to the user |
| Invite Redeemed | user.invite.redeemed | User redeemed invitation |
| User Added to Account | user.added | New user added to the account |
| User Added to Group | group.user.added | An existing user was added to a group |
| User Removed from Account | user.removed | User removed from the account |
| User Removed from Group | group.user.removed | An existing user was removed from a group |
| User License Created | user\_license.added | A new user license was consumed |
| User License Removed | user\_license.removed | A user license was removed from the seat count |
| Verification Email Confirmed | user.jit.email.confirmed | Email verification confirmed by user |
| Verification Email Sent | user.jit.email.sent | Email verification sent to user created via JIT |

### Project[​](#project "Direct link to Project")

| Event Name | Event Type | Description |
| --- | --- | --- |
| Project Added | project.added | New project added |
| Project Changed | project.changed | Project settings changed |
| Project Removed | project.removed | Project is removed |

### Permissions[​](#permissions "Direct link to Permissions")

| Event Name | Event Type | Description |
| --- | --- | --- |
| User Permission Added | permission.added | New user permissions are added |
| User Permission Removed | permission.removed | User permissions are removed |

### License[​](#license "Direct link to License")

| Event Name | Event Type | Description |
| --- | --- | --- |
| License Mapping Added | license\_map.added | New user license mapping is added |
| License Mapping Changed | license\_map.changed | User license mapping settings are changed |
| License Mapping Removed | license\_map.removed | User license mapping is removed |

### Connection[​](#connection "Direct link to Connection")

| Event Name | Event Type | Description |
| --- | --- | --- |
| Connection Added | connection.added | New Data Warehouse connection added |
| Connection Changed | connection.changed | Data Warehouse Connection settings changed |
| Connection Removed | connection.removed | Data Warehouse connection removed |

### Repository[​](#repository "Direct link to Repository")

| Event Name | Event Type | Description |
| --- | --- | --- |
| Repository Added | repository.added | New repository added |
| Repository Changed | repository.changed | Repository settings changed |
| Repository Removed | repository.removed | Repository removed |

### Credentials[​](#credentials "Direct link to Credentials")

| Event Name | Event Type | Description |
| --- | --- | --- |
| Credentials Added to Project | credentials.added | Project credentials added |
| Credentials Changed in Project | credentials.changed | Credentials changed in project |
| Credentials Removed from Project | credentials.removed | Credentials removed from project |

### Git integration[​](#git-integration "Direct link to Git integration")

| Event Name | Event Type | Description |
| --- | --- | --- |
| GitLab Application Changed | gitlab\_application.changed | GitLab configuration in dbt changed |

### Webhooks[​](#webhooks "Direct link to Webhooks")

| Event Name | Event Type | Description |
| --- | --- | --- |
| Webhook Subscriptions Added | webhook\_subscription.added | New webhook configured in settings |
| Webhook Subscriptions Changed | webhook\_subscription.changed | Existing webhook configuration altered |
| Webhook Subscriptions Removed | webhook\_subscription.removed | Existing webhook deleted |

### Semantic Layer[​](#semantic-layer "Direct link to Semantic Layer")

| Event Name | Event Type | Description |
| --- | --- | --- |
| Semantic Layer Config Added | semantic\_layer\_config.added | Semantic Layer config added |
| Semantic Layer Config Changed | semantic\_layer\_config.changed | Semantic Layer config (not related to credentials) changed |
| Semantic Layer Config Removed | semantic\_layer\_config.removed | Semantic Layer config removed |
| Semantic Layer Credentials Added | semantic\_layer\_credentials.added | Semantic Layer credentials added |
| Semantic Layer Credentials Changed | semantic\_layer\_credentials.changed | Semantic Layer credentials changed. Does not trigger semantic\_layer\_config.changed |
| Semantic Layer Credentials Removed | semantic\_layer\_credentials.removed | Semantic Layer credentials removed |

### Extended attributes[​](#extended-attributes "Direct link to Extended attributes")

| Event Name | Event Type | Description |
| --- | --- | --- |
| Extended Attribute Added | extended\_attributes.added | Extended attribute added to a project |
| Extended Attribute Changed | extended\_attributes.changed | Extended attribute changed or removed |

### Account-scoped personal access token[​](#account-scoped-personal-access-token "Direct link to Account-scoped personal access token")

| Event Name | Event Type | Description |
| --- | --- | --- |
| Account Scoped Personal Access Token Created | account\_scoped\_pat.created | An account-scoped PAT was created |
| Account Scoped Personal Access Token Deleted | account\_scoped\_pat.deleted | An account-scoped PAT was deleted |

### IP restrictions[​](#ip-restrictions "Direct link to IP restrictions")

| Event Name | Event Type | Description |
| --- | --- | --- |
| IP Restrictions Toggled | ip\_restrictions.toggled | IP restrictions feature enabled or disabled |
| IP Restrictions Rule Added | ip\_restrictions.rule.added | IP restriction rule created |
| IP Restrictions Rule Changed | ip\_restrictions.rule.changed | IP restriction rule edited |
| IP Restrictions Rule Removed | ip\_restrictions.rule.removed | IP restriction rule deleted |

### SCIM[​](#scim "Direct link to SCIM")

| Event Name | Event Type | Description |
| --- | --- | --- |
| User Creation | v1.events.account.UserAdded | New user created by SCIM service |
| User Update | v1.events.account.UserUpdated | User record updated by SCIM service |
| User Removal | v1.events.account.UserRemoved | User deleted by the SCIM service |
| Group Creation | v1.events.user\_group.Added | New group created by SCIM service |
| Group Update | v1.events.user\_group\_user.Changed | Group membership was updated by SCIM service |
| Group Removal | v1.events.user\_group.Removed | Group removed by SCIM service |

Searching the audit log[​](#searching-the-audit-log "Direct link to Searching the audit log")
---------------------------------------------------------------------------------------------

You can search the audit log to find a specific event or actor, which is limited to the ones listed in [Events in audit log](#events-in-audit-log). The audit log successfully lists historical events spanning the last 90 days. You can search for an actor or event using the search bar, and then narrow your results using the time window.

[![Use search bar to find content in the audit log](/img/docs/dbt-cloud/dbt-cloud-enterprise/audit-log-search.png?v=2 "Use search bar to find content in the audit log")](#)Use search bar to find content in the audit log

Exporting logs[​](#exporting-logs "Direct link to Exporting logs")
------------------------------------------------------------------

You can use the audit log to export all historical audit results for security, compliance, and analysis purposes. Events in the audit log are retained for at least 12 months.

* **For events within 90 days** — dbt will automatically display the 90-day selectable date range. Select **Export Selection** to download a CSV file of all the events that occurred in your organization within 90 days.
* **For events beyond 90 days** — Select **Export All**. The Account Admin or Account Viewer will receive an email link to download a CSV file of all the events that occurred in your organization.

[![View audit log export options](/img/docs/dbt-cloud/dbt-cloud-enterprise/audit-log-section.png?v=2 "View audit log export options")](#)View audit log export options

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/cloud/manage-access/audit-log.md)

Last updated on **Nov 19, 2025**

[Previous

About user access in dbt](/docs/cloud/manage-access/about-user-access)

* [Accessing the audit log](#accessing-the-audit-log)
* [Understanding the audit log](#understanding-the-audit-log)
  + [Event details](#event-details)
* [Audit log events](#audit-log-events)
  + [Authentication](#authentication)
  + [Environment](#environment)
  + [Jobs](#jobs)
  + [Service Token](#service-token)
  + [Group](#group)
  + [User](#user)
  + [Project](#project)
  + [Permissions](#permissions)
  + [License](#license)
  + [Connection](#connection)
  + [Repository](#repository)
  + [Credentials](#credentials)
  + [Git integration](#git-integration)
  + [Webhooks](#webhooks)
  + [Semantic Layer](#semantic-layer)
  + [Extended attributes](#extended-attributes)
  + [Account-scoped personal access token](#account-scoped-personal-access-token)
  + [IP restrictions](#ip-restrictions)
  + [SCIM](#scim)
* [Searching the audit log](#searching-the-audit-log)
* [Exporting logs](#exporting-logs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/cloud/manage-access/audit-log.md)

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