from regression1_abhisheks_e2etests_snowflake_automationjobs_project_duplicate_snowflake_sqlairflow_automation.utils import *

def Python_1(config_1, config_2, config_3, ti=None, params=None, **context):

    def return_method():
        print(f"{config_1},{config_2},{config_3}")

    import json
    from datetime import timedelta
    from airflow.operators.python import PythonOperator

    return PythonOperator(task_id = "Python_1", python_callable = return_method, show_return_value_in_logs = True)
