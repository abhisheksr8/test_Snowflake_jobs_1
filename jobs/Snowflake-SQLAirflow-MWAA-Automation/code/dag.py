import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from staging_abhisheks_e2etests_snowflake_automationjobs_project_snowflake_sqlairflow_mwaa_automation.tasks import (
    Model_0
)
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "staging_abhisheks_e2etests_Snowflake_AutomationJobs_Project_Snowflake_SQLAirflow_MWAA_Automation", 
    schedule_interval = "0 0 17 2 *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    Model_0_op = Model_0()
