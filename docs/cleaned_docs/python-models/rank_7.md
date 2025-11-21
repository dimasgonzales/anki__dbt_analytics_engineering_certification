Copy page

On this page

Supported features
==================

Learn about the features supported by the dbt Fusion engine, including requirements and limitations.

Requirements[​](#requirements "Direct link to Requirements")
------------------------------------------------------------

To use Fusion in your dbt project:

* You're using a supported adapter and authentication method:
   BigQuery

  + Service Account / User Token
  + Native OAuth
  + External OAuth
  + [Required permissions](/docs/core/connect-data-platform/bigquery-setup#required-permissions)

   Databricks

  + Service Account / User Token
  + Native OAuth

   Redshift

  + Username / Password
  + IAM profile

   Snowflake

  + Username / Password
  + Native OAuth
  + External OAuth
  + Key pair using a modern PKCS#8 method
  + MFA
* Have only SQL models defined in your project. Python models are not currently supported because Fusion cannot parse these to extract dependencies (refs) on other models.

Parity with dbt Core[​](#parity-with-dbt-core "Direct link to Parity with dbt Core")
------------------------------------------------------------------------------------

Our goal is for the dbt Fusion Engine to support all capabilities of the dbt Core framework, and then some. Fusion already supports many of the capabilities in dbt Core v1.9, and we're working fast to add more.

Note that we have removed some deprecated features and introduced more rigorous validation of erroneous project code. Refer to the [Upgrade guide](/docs/dbt-versions/core-upgrade/upgrading-to-fusion) for details.

Features and capabilities[​](#features-and-capabilities "Direct link to Features and capabilities")
---------------------------------------------------------------------------------------------------

* dbt Fusion Engine (built on Rust) gives your team up to 30x faster performance and comes with different features depending on where you use it.
* It powers both *engine-level* improvements (like faster compilation and incremental builds) and *editor-level* features (like IntelliSense, hover info, and inline errors) through the LSP.
* To learn about the LSP features supported across the dbt platform, refer to [About dbt LSP](/docs/about-dbt-lsp).
* To stay up-to-date on the latest features and capabilities, check out the [Fusion diaries](https://github.com/dbt-labs/dbt-fusion/discussions).

If you're not sure what features are available, check out the following table.

> ✅ = Available | 🟡 = Partial / at compile-time only | ❌ = Not available | Coming soon = Not yet available

| **Category / Capability** | **dbt Core** (self-hosted) | **Fusion CLI** (self-hosted) | **VS Code  + Fusion** | **dbt platform**\* |
| --- | --- | --- | --- | --- |
| **Engine performance** |  |  |  |  |
| SQL compilation | ✅ | ✅ | ✅ | ✅ |
| SQL compilation and parsing (SQL understanding) | ❌ | ✅ | ✅ | ✅ |
| Uses the dbt Fusion Engine | ❌  (Built on Python) | ✅ | ✅ | ✅ |
| Up to 30x faster parse / compile | ❌ | ✅ | ✅ | ✅ |
| Incremental compilation | ❌ | ❌ | ✅ | ✅ |
| **Editor and development experience** |  |  |  |  |
| IntelliSense / autocomplete / hover info | ❌ | ❌ | ✅ | ✅ |
| Inline errors (on save / in editor) | ❌ | 🟡 | ✅ | ✅ |
| Live CTE previews / compiled SQL view | ❌ | ❌ | ✅ | ✅ |
| Refactoring tools (rename model / column) | ❌ | ❌ | ✅ | Coming soon |
| Go-to definition / references | ❌ | ❌ | ✅ | Coming soon |
| Column-level lineage (in editor) | ❌ | ❌ | ✅ | Coming soon |
| Developer compare changes | ❌ | ❌ | Coming soon | Coming soon |
| **Platform and governance** |  |  |  |  |
| Advanced CI compare changes | ❌ | ❌ | ✅ | ✅ |
| dbt Mesh | ❌ | ❌ | ✅ | ✅ |
| State-aware orchestration (SAO) | ❌ | ❌ | ❌ | ✅ |
| Governance (PII / PHI tracking) | ❌ | ❌ | ❌ | Coming soon |
| CI/CD cost optimization (Slimmer CI) | ❌ | ❌ | ❌ | Coming soon |

\*Support for other dbt platform tools, like Semantic Layer and Catalog, is coming soon.

#### Additional considerations[​](#additional-considerations "Direct link to Additional considerations")

Here are some additional considerations if using the Fusion CLI without the VS Code extension or the VS Code extension without the Fusion CLI:

* **Fusion CLI** ([binary](/blog/dbt-fusion-engine-components))
  + Free to use and runs on the dbt Fusion Engine (distinct from dbt Core).
  + Benefits from Fusion engine’s performance for `parse`, `compile`, `build`, and `run`, but *doesn't* include visual and interactive [features](/docs/dbt-extension-features) like autocomplete, hover insights, lineage, and more.
  + Requires `profiles.yml` only (no `dbt_cloud.yml`).
* **dbt VS Code extension**
  + Free to use and runs on the dbt Fusion Engine; register your email within 14 days.
  + Benefits from Fusion engine’s performance for `parse`, `compile`, `build`, and `run`, and also includes visual and interactive [features](/docs/dbt-extension-features) like autocomplete, hover insights, lineage, and more.
  + Capped at 15 users per organization. See the [acceptable use policy](https://www.getdbt.com/dbt-assets/vscode-plugin-aup) for more information.
  + If you already have a dbt platform user account (even if a trial expired), sign in with the same email. Unlock or reset it if locked.
  + Requires both `profiles.yml` and `dbt_cloud.yml` files.

Limitations[​](#limitations "Direct link to Limitations")
---------------------------------------------------------

If your project is using any of the features listed in the following table, you can use Fusion, but you won't be able to fully migrate all your workloads because you have:

* Models that leverage specific materialization features may be unable to run or may be missing some desirable configurations.
* Tooling that expects dbt Core's exact log output. Fusion's logging system is currently unstable and incomplete.
* Workflows built around complementary features of the dbt platform (like model-level notifications, Advanced CI, and Semantic Layer) that Fusion does not yet support.

note

We have been moving quickly to implement many of these features ahead of General Availability. Read more about [the path to GA](/blog/dbt-fusion-engine-path-to-ga), and track our progress in the [`dbt-fusion` milestones](https://github.com/dbt-labs/dbt-fusion/milestones).

| Feature | This will affect you if... | GitHub issue |
| --- | --- | --- |
| [--store-failures](/reference/resource-configs/store_failures) | You use the --store-failures feature of dbt test to materialize the results of test queries in audit tables. | [dbt-fusion#15](https://github.com/dbt-labs/dbt-fusion/issues/15) |
| [--fail-fast](/reference/resource-configs/store_failures) | You use the --fail-fast flag to interrupt runs at the first sign of failure. | [dbt-fusion#18](https://github.com/dbt-labs/dbt-fusion/issues/18) |
| [microbatch incremental strategy](/docs/build/incremental-microbatch) | You are configuring models with materializations other than view, table, or incremental. You cannot yet run those models with Fusion, but you can run models using the standard materializations. | [dbt-fusion#12](https://github.com/dbt-labs/dbt-fusion/issues/12) |
| [--warn-error, --warn-error-options](/reference/global-configs/warnings) | You are upgrading all/specific warnings to errors, or silencing specific warnings, by configuring the warning event names. Fusion's logging system is incomplete and unstable, and so specific event names are likely to change. | [dbt-fusion#8](https://github.com/dbt-labs/dbt-fusion/issues/8) |
| [Advanced CI ("compare changes")](/docs/deploy/advanced-ci) | You use the "compare changes" feature of Advanced CI in the dbt platform. | [dbt-fusion#26](https://github.com/dbt-labs/dbt-fusion/issues/26) |
| [Model governance](/docs/mesh/govern/about-model-governance) (polish and feature completeness) | If you have models with a set `deprecation_date`, Fusion does not yet raise warnings about upcoming/past deprecations. Fusion’s logging system is currently incomplete and unstable. | [dbt-fusion#25](https://github.com/dbt-labs/dbt-fusion/issues/25) |
| Iceberg support (BigQuery) | You have configured models to be materialized as Iceberg tables, or you are defining `catalogs` in your BigQuery project to configure the external write location of Iceberg models. Fusion doesn't support these model configurations for BigQuery. | [dbt-fusion#947](https://github.com/dbt-labs/dbt-fusion/issues/947) |
| [Model-level notifications](/docs/deploy/model-notifications) | You are leveraging the dbt platform’s capabilities for model-level notifications in your workflows. Fusion currently supports job-level notifications. | [dbt-fusion#7](https://github.com/dbt-labs/dbt-fusion/issues/7) |
| [retry](/reference/commands/retry) | Fusion does not yet support the dbt retry CLI command, or "rerun failed job from point of failure." In deployment environments, using [state-aware orchestration](/docs/deploy/state-aware-about), you can simply rerun the job and Fusion will skip models that do not have fresh data or have not met their freshness.build\_after threshold since the last build | [dbt-fusion#21](https://github.com/dbt-labs/dbt-fusion/issues/21) |
| [`state:modified.<subselector>` methods](/reference/node-selection/methods#state) | You rely on granular "subselectors" because state:modified is insufficiently precise. Fusion’s state detection is smarter out-of-the-box; give it a try! | [dbt-fusion#33](https://github.com/dbt-labs/dbt-fusion/issues/33) |
| [dbt-docs documentation site](/docs/build/view-documentation#dbt-docs) and ["docs generate/serve" commands](/reference/commands/cmd-docs) | Fusion does not yet support a local experience for generating, hosting, and viewing documentation, as dbt Core does via dbt-docs (static HTML site). We intend to support such an experience by GA. If you need to generate and host local documentation, you should continue generating the catalog by running dbt docs generate with dbt Core. | [dbt-fusion#9](https://github.com/dbt-labs/dbt-fusion/issues/9) |
| [Programmatic invocations](/reference/programmatic-invocations) | You use dbt Core’s Python API for triggering invocations and registering callbacks on events/logs. Note that Fusion’s logging system is incomplete and unstable. | [dbt-fusion#10](https://github.com/dbt-labs/dbt-fusion/issues/10) |
| [Semantic Layer](/docs/use-dbt-semantic-layer/dbt-sl): development + saved\_query exports | If you actively develop new semantic objects (semantic\_models, metrics, saved\_queries), or change existing objects in your dbt project, you should do this with dbt Core rather than Fusion, because Fusion does not yet produce semantic\_manifest.json (the interface to MetricFlow). If you use the "exports" feature of saved queries, this is not yet supported in Fusion, so you should continue running your jobs on dbt Core. | [dbt-fusion#40](https://github.com/dbt-labs/dbt-fusion/issues/40) |
| [Logging system](/reference/events-logging) | You have scripts, workflows, or other integrations that rely on specific log messages (structured or plaintext). At present, Fusion’s logging system is incomplete and unstable. It is also not our goal to provide full conformance between dbt Core logging and Fusion logging. | [dbt-fusion#7](https://github.com/dbt-labs/dbt-fusion/issues/7) |
| [Linting via SQLFluff](/docs/deploy/continuous-integration#to-configure-sqlfluff-linting) | You use SQLFluff for linting in your development or CI workflows. Eventually, we plan to build linting support into Fusion directly, since the engine has SQL comprehension capabilities. In the meantime, you can continue using the dbt Core + SQLFluff integration. dbt Cloud will do exactly this in the Cloud IDE / Studio + CI jobs. | [dbt-fusion#11](https://github.com/dbt-labs/dbt-fusion/issues/11) |
| [Active and auto exposures](/docs/cloud-integrations/downstream-exposures) | You rely on auto exposures to pull downstream assets (like Tableau dashboards) into dbt lineage, or on active exposures to proactively refresh downstream assets (like Tableau extracts) during scheduled jobs.    Fusion doesn't support active and auto exposures yet. | [dbt-fusion#704](https://github.com/dbt-labs/dbt-fusion/issues/704) |
| [`{{ graph }}`](/reference/dbt-jinja-functions/graph) - `raw_sql` attribute (e.g. specific models in [dbt\_project\_evaluator](https://hub.getdbt.com/dbt-labs/dbt_project_evaluator/latest/)) | You access the `raw_sql` / `raw_code` attribute of the `{{ graph }}` context variable, which Fusion stubs with an empty value at runtime. If you access this attribute, your code will not fail, but it will return different results. This is used in three quality checks within the [`dbt_project_evaluator` package](https://hub.getdbt.com/dbt-labs/dbt_project_evaluator/latest/). We intend to find a more-performant mechanism for Fusion to provide this information in the future. | Coming soon |
| Externally orchestrated jobs | You use a third-party orchestrator (like Astronomer-Cosmos) that depends on a dbt manifest produced by dbt Core. Many of these integrations don't yet support manifests generated by Fusion. However, Fusion does support external orchestrators that integrate through the dbt platform run job API. | Coming soon |

More information about Fusion[​](#more-information-about-fusion "Direct link to More information about Fusion")
---------------------------------------------------------------------------------------------------------------

Fusion marks a significant update to dbt. While many of the workflows you've grown accustomed to remain unchanged, there are a lot of new ideas, and a lot of old ones going away. The following is a list of the full scope of our current release of the Fusion engine, including implementation, installation, deprecations, and limitations:

* [About the dbt Fusion engine](/docs/fusion/about-fusion)
* [About the dbt extension](/docs/about-dbt-extension)
* [New concepts in Fusion](/docs/fusion/new-concepts)
* [Supported features matrix](/docs/fusion/supported-features)
* [Installing Fusion CLI](/docs/fusion/install-fusion)
* [Installing VS Code extension](/docs/install-dbt-extension)
* [Fusion release track](/docs/dbt-versions/upgrade-dbt-version-in-cloud#dbt-fusion-engine)
* [Quickstart for Fusion](/guides/fusion?step=1)
* [Upgrade guide](/docs/dbt-versions/core-upgrade/upgrading-to-fusion)
* [Fusion licensing](http://www.getdbt.com/licenses-faq)

### Package support[​](#package-support "Direct link to Package support")

The following packages are verified and supported on the dbt Fusion Engine:

* [AxelThevenot/dbt\_assertions](https://github.com/AxelThevenot/dbt-assertions)
* [Datavault-UK/automate\_dv](https://github.com/Datavault-UK/dbtvault.git)
* [dbt-labs/audit\_helper](https://github.com/dbt-labs/dbt-audit-helper.git)
* [dbt-labs/codegen](https://github.com/dbt-labs/dbt-codegen.git)
* [dbt-labs/dbt\_project\_evaluator](https://github.com/dbt-labs/dbt-project-evaluator.git)
* [dbt-labs/dbt\_utils](https://github.com/dbt-labs/dbt-utils.git)
* [elementary-data/elementary](https://github.com/elementary-data/dbt-data-reliability.git)
* [entechlog/dbt\_snow\_mask](https://github.com/entechlog/dbt-snow-mask.git)
* [fivetran/ad\_reporting](https://github.com/fivetran/dbt_ad_reporting.git)
* [fivetran/facebook\_ads](https://github.com/fivetran/dbt_facebook_ads.git)
* [fivetran/fivetran\_log](https://github.com/fivetran/dbt_fivetran_log.git)
* [fivetran/fivetran\_utils](https://github.com/fivetran/dbt_fivetran_utils.git)
* [fivetran/google\_ads](https://github.com/fivetran/dbt_google_ads.git)

Additionally, the Fivetran `source` and `transformation` packages have been combined into a single package. If you manually installed source packages like `fivetran/github_source`, you need to ensure `fivetran/github` is installed and deactivate the transformation models.