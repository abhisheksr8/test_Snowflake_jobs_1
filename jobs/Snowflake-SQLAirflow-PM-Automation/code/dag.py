import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from f0buwu40ldcmqcjyflx5yq_.tasks import Email_1, HTTPSensor_1, Model_0, S3FileSensor_1, Slack_1
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "f0buWu40lDcMQCjyFLx5YQ_", 
    schedule_interval = "0 0 17 2 *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True, "pool" : "BOQhdxeL"}, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2034, 9, 17, tz = "UTC"), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    Model_0_op = Model_0()
    Slack_1_op = Slack_1()
    S3FileSensor_1_op = S3FileSensor_1()
    HTTPSensor_1_op = HTTPSensor_1()
    Email_1_op = Email_1()
    Model_0_op >> [Email_1_op, HTTPSensor_1_op, S3FileSensor_1_op, Slack_1_op]
