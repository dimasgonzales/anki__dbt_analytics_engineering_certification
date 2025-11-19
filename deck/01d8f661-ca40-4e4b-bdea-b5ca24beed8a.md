---
uuid: 01d8f661-ca40-4e4b-bdea-b5ca24beed8a
guid: rG!*ydqeW`
tags:
  - jinja
citations:
  - https://docs.getdbt.com/reference/dbt-jinja-functions/run_query
---

<front>
How can you execute a SQL query against your data warehouse using Jinja?
</front>

---

<back>

`run_query('query string')`. Note that `run_query` doesn't begin a transaction automatically; if you want transaction behavior, the query string needs to explicitly contain the relevant begin/commit/rollback commands for your database.  
  
`run_query` is a nice wrapper around the more flexible (but more complicated/clunkier) `statement` block

</back>
