---
tags:
- card_type/factual
- debugging/compiled-code
- development/cli-commands
- state/selectors
citations:
  - docs/site_docs.getdbt.com/citations/docs_getdbt_com_reference_node_selection_methods.md
guid: bZ`r/hy8t=
source: apkg
uuid: efceb7cd-48c3-5bb2-8fb3-d4f94fc6b954
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly demonstrates using the 'test_name' selector with 'dbt test --select' to run all instances of a specific generic test, matching the answer's syntax."
  citation:
    quote: "dbt test --select \"test_name:unique\"            # run all instances of the `unique` test"
    is_quote_valid: true
---

<front>

How can you run all instances of a particular generic test?

</front>

---

<back>

```
dbt test --select test_name:<generic test name>
```

</back>
