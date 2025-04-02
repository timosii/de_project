from datetime import datetime
from airflow import DAG
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from pendulum import datetime,duration


default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 3, 30),
}

with DAG(
    "daily_dwh_update",
    default_args=default_args,
    schedule_interval="0 8 * * *",
    catchup=False,
) as dag:
    
    wait_ingesting = ExternalTaskSensor(
        task_id='wait_data_ingestion',
        external_dag_id='daily_data_ingestion',
        external_task_id='daily_data_ingestion',
        timeout=duration(hours=2),
        poke_interval=duration(minutes=1),
        mode='reschedule'
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command='dbt build --project-dir /opt/airflow/breast_cancer --profiles-dir /opt/airflow/.dbt'
    )

    (
        wait_ingesting >> dbt_run
    )