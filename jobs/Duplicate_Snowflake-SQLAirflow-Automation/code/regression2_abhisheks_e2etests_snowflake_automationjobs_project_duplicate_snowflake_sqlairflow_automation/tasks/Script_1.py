from regression2_abhisheks_e2etests_snowflake_automationjobs_project_duplicate_snowflake_sqlairflow_automation.utils import *

def Script_1():
    from airflow.operators.bash import BashOperator

    return BashOperator(task_id = "Script_1", bash_command = "ls -ltr\n", )
