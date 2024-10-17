from f0buwu40ldcmqcjyflx5yq_.utils import *

def Slack_1():
    from airflow.providers.slack.operators.slack import SlackAPIPostOperator
    from datetime import timedelta

    return SlackAPIPostOperator(
        task_id = "Slack_1",
        text = "Test Automation Airflow",
        channel = "abhyslackpub",
        slack_conn_id = "Kz0VaT1RbgZ6QSdK_25Ak",
    )
