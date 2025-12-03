---
tags:
- card_type/scenario
- development/cli-commands
- state/selectors
- state/state-concepts
citations:
- cleaned_docs/grants/rank_6.md
guid: 4004aa9f67
source: llm
uuid: b3bb879a-ca7d-5ef4-8dab-d8f26adfd9ed
---

<front>

You are configuring a CI/CD pipeline and want to minimize costs by only running models that have changed in the PR, plus their downstream dependencies. What command ensures this 'Slim CI' behavior?

</front>

---

<back>

Use `dbt build` with the `state:modified+` selector. The `+` ensures that any downstream models dependent on the changes are also built and tested to prevent regressions.

```bash
dbt build --select "state:modified+" --state path/to/prod_manifest
```

</back>
