from regression2_abhisheks_e2etests_snowflake_automationjobs_project_snowflake_sqlairflow_automation.utils import *

def Branch_1():

    def which_gem_to_run():
        return "Python_0"

    from datetime import timedelta
    from airflow.operators.python import BranchPythonOperator

    return BranchPythonOperator(task_id = "Branch_1", python_callable = which_gem_to_run, )
