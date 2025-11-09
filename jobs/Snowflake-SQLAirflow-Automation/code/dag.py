import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from performance_abhisheks_e2etests_snowflake_automationjobs_project_snowflake_sqlairflow_automation.tasks import (
    Branch_1,
    ForEachLoop_1_tg,
    Model_1,
    Python_0,
    Python_3,
    Script_1,
    TaskGroup_1_tg
)
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "performance_abhisheks_e2etests_Snowflake_AutomationJobs_Project_Snowflake_SQLAirflow_Automation", 
    schedule_interval = "0 0 17 2 *", 
    default_args = {"owner" : "Prophecy", "retries" : 0, "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    Branch_1_op = Branch_1()
    Python_3_op = Python_3()
    Model_1_op = Model_1()
    Python_0_op = Python_0()
    ForEachLoop_1_op = ForEachLoop_1_tg.expand(value = Python_0_op.output)
    Script_1_op = Script_1()
    TaskGroup_1_op = TaskGroup_1_tg()
    Python_0_op >> [ForEachLoop_1_op, TaskGroup_1_op]
    Model_1_op >> Script_1_op
    Branch_1_op >> [Python_0_op, Python_3_op]
