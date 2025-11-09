from airflow.decorators import task_group
from .ForEachLoop_1_tasks import *
from performance_abhisheks_e2etests_snowflake_automationjobs_project_duplicate_snowflake_sqlairflow_automation.utils import *

@task_group(group_id = "ForEachLoop_1", default_args = {})
def ForEachLoop_1_tg(value):

    @task(task_id = "Python_1")
    def Python_1_op(value, **context):
        return Python_1(value["c1_data"][0]["data"], value["c2_data"][0]["data"], value["c3_data"], **context)\
            .execute(context)

    Python_1_call = Python_1_op(value)
