Copy page

On this page

Deploy your metrics [Starter](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")
============================================================================================================================================================================================================================================================================

This section explains how you can perform a job run in your deployment environment in dbt to materialize and deploy your metrics. Currently, the deployment environment is only supported.

1. Once you’ve [defined your semantic models and metrics](/guides/sl-snowflake-qs?step=10), commit and merge your metric changes in your dbt project.
2. In dbt, create a new [deployment environment](/docs/deploy/deploy-environments#create-a-deployment-environment) or use an existing environment on dbt 1.6 or higher.

   * Note — Deployment environment is currently supported (*development experience coming soon*)
3. To create a new environment, navigate to **Deploy** in the navigation menu, select **Environments**, and then select **Create new environment**.
4. Fill in your deployment credentials with your Snowflake username and password. You can name the schema anything you want. Click **Save** to create your new production environment.
5. [Create a new deploy job](/docs/deploy/deploy-jobs#create-and-schedule-jobs) that runs in the environment you just created. Go back to the **Deploy** menu, select **Jobs**, select **Create job**, and click **Deploy job**.
6. Set the job to run a `dbt parse` job to parse your projects and generate a [`semantic_manifest.json` artifact](/reference/artifacts/sl-manifest) file. Although running `dbt build` isn't required, you can choose to do so if needed.

   note

   If you are on the dbt Fusion engine, add the `dbt docs generate` command to your job to successfully deploy your metrics.
7. Run the job by clicking the **Run now** button. Monitor the job's progress in real-time through the **Run summary** tab.

   Once the job completes successfully, your dbt project, including the generated documentation, will be fully deployed and available for use in your production environment. If any issues arise, review the logs to diagnose and address any errors.

What’s happening internally?

* Merging the code into your main branch allows dbt to pull those changes and build the definition in the manifest produced by the run.
* Re-running the job in the deployment environment helps materialize the models, which the metrics depend on, in the data platform. It also makes sure that the manifest is up to date.
* The Semantic Layer APIs pull in the most recent manifest and enables your integration to extract metadata from it.

Next steps[​](#next-steps "Direct link to Next steps")
------------------------------------------------------

After you've executed a job and deployed your Semantic Layer:

* Discover the [available integrations](/docs/cloud-integrations/avail-sl-integrations), such as Tableau, Google Sheets, Microsoft Excel, and more.
* Start querying your metrics with the [API query syntax](/docs/dbt-cloud-apis/sl-jdbc#querying-the-api-for-metric-metadata).

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* If you haven't already, learn how to [build your metrics and semantic models](/docs/build/build-metrics-intro) in your development tool of choice.