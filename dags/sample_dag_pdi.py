
from datetime import time, timedelta

from airflow import DAG
from airflow.utils.dates import days_ago

from airflow_pentaho.operators.carte import CarteJobOperator
from airflow_pentaho.operators.carte import CarteTransOperator


DAG_NAME = 'pdi_flow'
DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'retries': 3,
    'retry_delay': timedelta(minutes=10),
    'email_on_failure': False,
    'email_on_retry': False
}

with DAG(dag_id=DAG_NAME,
         default_args=DEFAULT_ARGS,
         dagrun_timeout=timedelta(hours=2),
         schedule_interval=timedelta(minutes=1)) as dag:


    job1 = CarteJobOperator(
        dag=dag,
        task_id='pass_arguments',
        job='/data-integration/samples/jobs/arguments2/pass_arguments.kjb',
        )

    job2 = CarteJobOperator(
        dag=dag,
        task_id='shell_for_every_row',
        job='/data-integration/samples/jobs/shell for every row/shell for every row.kjb',
        )

        

       



    job1 >> job2 