---
tags:
- card_type/factual
- development/cli-commands
- development/project-config
- state/selectors
citations:
- cleaned_docs/project-config/rank_7.md
guid: 359019d817
source: llm
uuid: b8e36f4b-fe6d-580c-afaf-dde8fcbae1a3
claim_meta:
  verdict: NOT_FOUND
  explanation: "The reference text explicitly mentions 'model-paths' as a key in 'dbt_project.yml' for directory locations, but does not provide evidence for 'seed-paths' or 'test-paths', nor does it specify that these keys accept lists of directory strings. Therefore, the answer cannot be fully verified based on the provided text."
  citation:
    quote: "Flags that tell dbt where to find project resources (for example, `model-paths`) are set in `dbt_project.yml`, but as a top-level key, outside the `flags` dictionary;"
    is_quote_valid: true
---

<front>

Which keys in `dbt_project.yml` represent the configuration for overriding default directory locations for models, seeds, and tests?

</front>

---

<back>

The keys are `model-paths`, `seed-paths`, and `test-paths` (note the plural 'paths'). These accept lists of directory strings.

```yaml
model-paths: ["models"]
seed-paths: ["seeds"]
```

</back>
