from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="air_quality_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    extract_task = BashOperator(
        task_id="extract_data",
        bash_command="cd /Users/alphadiallo/air-quality-pipeline && python scripts/extract.py",
    )

    transform_task = BashOperator(
        task_id="transform_data",
        bash_command="cd /Users/alphadiallo/air-quality-pipeline && python scripts/transform.py",
    )

    load_task = BashOperator(
        task_id="load_data",
        bash_command="cd /Users/alphadiallo/air-quality-pipeline && python scripts/load.py",
    )

    extract_task >> transform_task >> load_task