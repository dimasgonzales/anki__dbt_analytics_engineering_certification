Copy page

On this page

About Hybrid projects [Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")
===========================================================================================================

With Hybrid projects, your organization can adopt complementary dbt Core and dbt workflows (where some teams deploy projects in dbt Core and others in dbt) and seamlessly integrate these workflows by automatically uploading dbt Core [artifacts](/reference/artifacts/dbt-artifacts) into dbt.

Available in public preview

Hybrid projects is available in public preview to [dbt Enterprise accounts](https://www.getdbt.com/pricing).

dbt Core users can seamlessly upload [artifacts](/reference/artifacts/dbt-artifacts) like [run results.json](/reference/artifacts/run-results-json), [manifest.json](/reference/artifacts/manifest-json), [catalog.json](/reference/artifacts/catalog-json), [sources.json](/reference/artifacts/sources-json), and so on — into dbt after executing a run in the dbt Core command line interface (CLI), which helps:

* Collaborate with dbt + dbt Core users by enabling them to visualize and perform [cross-project references](/docs/mesh/govern/project-dependencies#how-to-write-cross-project-ref) to dbt models that live in Core projects.
* (Coming soon) New users interested in the [Canvas](/docs/cloud/canvas) can build off of dbt models already created by a central data team in dbt Core rather than having to start from scratch.
* dbt Core and dbt users can navigate to [Catalog](/docs/explore/explore-projects) and view their models and assets. To view Catalog, you must have a [read-only seat](/docs/cloud/manage-access/seats-and-users).

Prerequisites[​](#prerequisites "Direct link to Prerequisites")
---------------------------------------------------------------

To upload artifacts, make sure you meet these prerequisites:

* Your organization is on a [dbt Enterprise+ plan](https://www.getdbt.com/pricing)
* You're on [dbt's release tracks](/docs/dbt-versions/cloud-release-tracks) and your dbt Core project is on dbt v1.10 or higher
* Updated your existing dbt Core project with latest changes and [configured it with model access](/docs/deploy/hybrid-setup#make-dbt-core-models-public):
  + Ensure models that you want to share with other dbt projects use `access: public` in their model configuration. This makes the models more discoverable and shareable
  + Learn more about [access modifier](/docs/mesh/govern/model-access#access-modifiers) and how to set the [`access` config](/reference/resource-configs/access)
* Update [dbt permissions](/docs/cloud/manage-access/enterprise-permissions) to create a new project in dbt

**Note:** Uploading artifacts doesn't count against dbt run slots.