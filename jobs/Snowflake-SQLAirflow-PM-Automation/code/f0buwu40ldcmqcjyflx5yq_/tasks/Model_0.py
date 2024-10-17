from f0buwu40ldcmqcjyflx5yq_.utils import *

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
          "is_prophecy_managed": True,
          "run_deps": False,
          "run_seeds": True,
          "run_parents": False,
          "run_children": False,
          "run_tests": True,
          "run_mode": "model",
          "entity_kind": None,
          "entity_name": "test_Automation_Snowflake_jobs_model",
          "project_id": "1789",
          "git_entity": "branch",
          "git_entity_value": "testBranchSnowflakeJobs",
          "git_ssh_url": "https://github.com/abhisheksr8/test_Snowflake_jobs_1.git",
          "git_sub_path": "",
          "select": "",
          "threads": "",
          "exclude": "",
          "run_props": " --profile run_profile",
          "envs": {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy"}, 
          "git_token_secret": "nvUzJurwO2CsmkhRBTtASA_", 
          "dbt_profile_secret": "pUPpt2B4YfsUg45OWj_hy"
        },
    )
