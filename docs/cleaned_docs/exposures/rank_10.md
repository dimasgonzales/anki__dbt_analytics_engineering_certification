Copy page

On this page

Visualize downstream exposures [Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")
=======================================================================================================================================================================================================

Downstream exposures integrate natively with Tableau (Power BI coming soon) and auto-generate downstream lineage in Catalog for a richer experience.

As a data team, it’s critical that you have context into the downstream use cases and users of your data products. By leveraging downstream [exposures](/docs/build/exposures) automatically, data teams can:

* Gain a better understanding of how models are used in downstream analytics, improving governance and decision-making.
* Reduce incidents and optimize workflows by linking upstream models to downstream dependencies.
* Automate exposure tracking for supported BI tools, ensuring lineage is always up to date.
* [Orchestrate exposures](/docs/cloud-integrations/orchestrate-exposures) to refresh the underlying data sources during scheduled dbt jobs, improving timeliness and reducing costs. Orchestrating exposures is essentially a way to ensure that your BI tools are updated regularly by using the [dbt job scheduler](/docs/deploy/deployments).
  + For more info on the differences between visualizing and orchestrating exposures, see [Visualize and orchestrate downstream exposures](/docs/cloud-integrations/downstream-exposures).

To configure downstream exposures automatically from dashboards in Tableau, prerequisites, and more — refer to [Configure downstream exposures](/docs/cloud-integrations/downstream-exposures-tableau).

### Supported plans[​](#supported-plans "Direct link to Supported plans")

Downstream exposures is available on all dbt [Enterprise-tier plans](https://www.getdbt.com/pricing/). Currently, you can only connect to a single Tableau site on the same server.

Tableau Server

If you're using Tableau Server, you need to [allowlist dbt's IP addresses](/docs/cloud/about-cloud/access-regions-ip-addresses) for your dbt region.

View downstream exposures[​](#view-downstream-exposures "Direct link to View downstream exposures")
---------------------------------------------------------------------------------------------------

After setting up downstream exposures in dbt, you can view them in [Catalog](/docs/explore/explore-projects) for a richer experience.

Navigate to Catalog by clicking on the **Explore** link in the navigation. From the **Overview** page, you can view downstream exposures from a couple of places: