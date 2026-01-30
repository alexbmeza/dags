from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner':'alex',
    'depends_on_past': False,
    'email':['alex.boava@gmail.com'],
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':2,
    'retry_delay': timedelta(seconds=10)
}

dag = DAG (
    'teste_dag_1',
    default_args= default_args,
    start_date=datetime(2026,1,17),
    schedule='@daily',
    tags=['treinamento', 'teste','bash']
)

t1 =  BashOperator(
    task_id = 'print_date',
    bash_command='date',
    dag=dag
)   

t2 = BashOperator(
    task_id='sleep',
    depends_on_past= False,
    bash_command = 'sleep 10',
    retries=3,
    dag=dag

)

t1 >> [t2]