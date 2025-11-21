Copy page

On this page

About dbt docs commands
=======================

`dbt docs` has two supported subcommands: `generate` and `serve`.

### dbt docs generate[​](#dbt-docs-generate "Direct link to dbt docs generate")

The command is responsible for generating your project's documentation website by

1. Copying the website `index.html` file into the `target/` directory.
2. Compiling the resources in your project, so that their `compiled_code` will be included in [`manifest.json`](/reference/artifacts/manifest-json).
3. Running queries against database metadata to produce the [`catalog.json`](/reference/artifacts/catalog-json) file, which contains metadata about the tables and views produced by the models in your project.

**Example**:

```
dbt docs generate
```

Use the `--select` argument to limit the nodes included within `catalog.json`. When this flag is provided, step (3) will be restricted to the selected nodes. All other nodes will be excluded. Step (2) is unaffected.

**Example**:

```
dbt docs generate --select +orders
```

Use the `--no-compile` argument to skip re-compilation. When this flag is provided, `dbt docs generate` will skip step (2) described above.

**Example**:

```
dbt docs generate --no-compile
```

Use the `--empty-catalog` argument to skip running the database queries to populate `catalog.json`. When this flag is provided, `dbt docs generate` will skip step (3) described above.

This is not recommended for production environments, as it means that your documentation will be missing information gleaned from database metadata (the full set of columns in each table, and statistics about those tables). It can speed up `docs generate` in development, when you just want to visualize lineage and other information defined within your project. To learn how to build your documentation in dbt, refer to [build your docs in dbt](/docs/explore/build-and-view-your-docs).

**Example**:

```
dbt docs generate --empty-catalog
```

**Example**:

Use the `--static` flag to generate the docs as a static page for hosting on a cloud storage provider. The `catalog.json` and `manifest.json` files will be inserted into the `index.html` file, creating a single page easily shared via email or file-sharing apps.

```
dbt docs generate --static
```

### dbt docs serve[​](#dbt-docs-serve "Direct link to dbt docs serve")

This command starts a webserver on port 8080 to serve your documentation locally and opens the documentation site in your default browser. The webserver is rooted in your `target/` directory. Be sure to run `dbt docs generate` before `dbt docs serve` because the `generate` command produces a [catalog metadata artifact](/reference/artifacts/catalog-json) that the `serve` command depends upon. You will see an error message if the catalog is missing.

Use the `dbt docs serve` command if you're developing locally with the [Cloud CLI](/docs/cloud/cloud-cli-installation) or [dbt Core](/docs/core/installation-overview). The [Studio IDE](/docs/cloud/dbt-cloud-ide/develop-in-the-cloud) doesn't support this command.

**Usage:**

You may specify a different port using the `--port` flag.

**Example**:

```
dbt docs serve --port 8001
```