from test_abhisheks_e2etests_snowflake_automationjobs_project_snowflake_sqlairflow_automation.utils import *

def Model_1():
    from airflow.operators.python import PythonOperator
    from datetime import timedelta
    import os
    import zipfile
    import tempfile

    return PythonOperator(
        task_id = "Model_1",
        python_callable = invoke_dbt_runner,
        op_kwargs = {
          "is_adhoc_run_from_same_project": False,
          "is_prophecy_managed": False,
          "run_deps": True,
          "run_seeds": True,
          "run_parents": False,
          "run_children": False,
          "run_tests": True,
          "run_mode": "project",
          "entity_kind": None,
          "entity_name": None,
          "project_id": "64623",
          "git_entity": "commit",
          "git_entity_value": "testBranchSnowflakeJobs",
          "git_ssh_url": "https://github.com/abhisheksr8/test_Snowflake_jobs_1.git",
          "git_sub_path": "",
          "select": "",
          "threads": "",
          "exclude": "",
          "run_props": " --profile run_profile_snowflake",
          "envs": {
            "DBT_DATABRICKS_INVOCATION_ENV": "prophecy", 
            "DBT_PROFILES_DIR": "/home/airflow/gcs/data", 
            "DBT_SEND_ANONYMOUS_USAGE_STATS": "false", 
            "DBT_FULL_REFRESH": "true"
          }
        },
        retries = 1, 
        retry_delay = timedelta(minutes = 1.0)
    )
