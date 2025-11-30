from staging_abhisheks_e2etests_snowflake_automationjobs_project_snowflake_sqlairflow_mwaa_automation.utils import *

def Model_0():
    from airflow.operators.python import PythonOperator
    from datetime import timedelta
    import os
    import zipfile
    import tempfile

    return PythonOperator(
        task_id = "Model_0",
        python_callable = invoke_dbt_runner,
        op_kwargs = {
          "is_adhoc_run_from_same_project": False,
          "is_prophecy_managed": False,
          "run_deps": False,
          "run_seeds": True,
          "run_parents": False,
          "run_children": False,
          "run_tests": True,
          "run_mode": "model",
          "entity_kind": "model",
          "entity_name": "test_Automation_Snowflake_jobs_model",
          "project_id": "68302",
          "git_entity": "tag",
          "git_entity_value": "Snowflake_AutomationJobs_Project/1.0",
          "git_ssh_url": "https://github.com/abhisheksr8/test_Snowflake_jobs_1.git",
          "git_sub_path": "",
          "select": "",
          "threads": "",
          "exclude": "",
          "run_props": " --profile run_profile_snowflake",
          "envs": {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy", "DBT_PROFILES_DIR" : "/usr/local/airflow/dags"}
        },
        retries = 1, 
        max_retry_delay = timedelta(minutes = 1.0)
    )
