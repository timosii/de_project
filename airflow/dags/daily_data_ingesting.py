from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from app.data_ingest import data_ingest


default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 3, 30),
}

with DAG(
    "daily_data_ingestion",
    default_args=default_args,
    schedule_interval="0 8 * * *",
    catchup=False,
) as dag:
    
    @task
    def daily_data_ingestion():
        data_ingest()

    daily_data_ingestion()