---
uuid: 4da10e33-d60c-43fc-bf9d-34ff8d7daa5d
guid: Kn($<a{Fl&
tags:
  - dbt_project.yml
citations:
  - https://docs.getdbt.com/reference/project-configs/clean-targets
---

<front>
What **dbt\_project.yml** field is used to specify a custom list of directories to be removed by the `dbt clean` command? What is the default? What is the use case?
</front>

---

<back>

**clean-targets**. By default, `dbt clean` will remove files in your `target-path`. The main use case (recommended by dbtlabs) is to "upgrade" `dbt clean` to also remove installed packages and logs, by adding the values of your `log-path` and `packages-install-path` to the `clean-targets` list.

</back>
