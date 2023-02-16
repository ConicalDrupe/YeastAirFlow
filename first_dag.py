from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def first_execute():
    print("Hello World")
    return "Hello World"

#make file name same as dag_id
with DAG(
        dag_id="first_dag"
        schedule_interval="@daily"
        default_arge={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5)
            "start_date": datetime(2020, 1, 1)
            },
            catchup=False) as f:

first_excecute = PythonOperator(
    task_id="first_execute"
    python_callable=first_execute,
    )    