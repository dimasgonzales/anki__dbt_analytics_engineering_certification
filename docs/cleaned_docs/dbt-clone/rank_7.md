Copy page

On this page

About state in dbt
==================

One of the greatest underlying assumptions about dbt is that its operations should be **stateless** and **idempotent**. That is, it doesn't matter how many times a model has been run before, or if it has ever been run before. It doesn't matter if you run it once or a thousand times. Given the same raw data, you can expect the same transformed result. A given run of dbt doesn't need to "know" about *any other* run; it just needs to know about the code in the project and the objects in your database as they exist *right now*.

That said, dbt does store "state" — a detailed, point-in-time view of project resources (also referred to as nodes), database objects, and invocation results — in the form of its [artifacts](/docs/deploy/artifacts). If you choose, dbt can use these artifacts to inform certain operations. Crucially, the operations themselves are still stateless and idempotent: given the same manifest and the same raw data, dbt will produce the same transformed result.

dbt can leverage artifacts from a prior invocation as long as their file path is passed to the `--state` flag. This is a prerequisite for:

  by comparing code in the current project against the state manifest.
* The [`dbt clone` command](/reference/commands/clone), whereby dbt can clone nodes based on their location in the manifest provided to the `--state` flag.

Together, the [`state`](/reference/node-selection/methods#state) selector and deferral enable ["slim CI"](/best-practices/best-practice-workflows#run-only-modified-models-to-test-changes-slim-ci). We expect to add more features in future releases that can leverage artifacts passed to the `--state` flag.

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------