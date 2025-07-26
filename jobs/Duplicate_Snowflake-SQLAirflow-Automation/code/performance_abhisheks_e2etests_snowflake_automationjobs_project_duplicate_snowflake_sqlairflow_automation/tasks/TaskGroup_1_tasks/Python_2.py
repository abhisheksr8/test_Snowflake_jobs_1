from performance_abhisheks_e2etests_snowflake_automationjobs_project_duplicate_snowflake_sqlairflow_automation.utils import *

def Python_2():

    def returnString():
        return "Hello Sir"

    import json
    from datetime import timedelta
    from airflow.operators.python import PythonOperator

    return PythonOperator(task_id = "Python_2", python_callable = returnString, show_return_value_in_logs = True)
