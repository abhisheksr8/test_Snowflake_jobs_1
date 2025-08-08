from airflow.decorators import task_group
from .TaskGroup_1_tasks import *
from test_abhisheks_e2etests_snowflake_automationjobs_project_duplicate_snowflake_sqlairflow_automation.utils import *

@task_group(group_id = "TaskGroup_1", default_args = {})
def TaskGroup_1_tg():
    Python_2_op = Python_2()
