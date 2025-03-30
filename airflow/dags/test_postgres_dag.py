from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

def test_postgres_connection():
    hook = PostgresHook(postgres_conn_id="postgres_default")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    print("PostgreSQL connection test:", result)

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    "test_postgres_connection",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:
    test_task = PythonOperator(
        task_id="test_postgres_connection",
        python_callable=test_postgres_connection,
    )