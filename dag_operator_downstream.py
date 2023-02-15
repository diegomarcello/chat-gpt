from airflow import DAG
from airflow.operators.bigquery_check_operator import BigQueryCheckOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 2, 15),
}

def process_bq_check(**context):
    if context['task_instance'].xcom_pull(task_ids='check_bq_table'):
        print('The BigQueryCheckOperator returned rows!')
    else:
        print('The BigQueryCheckOperator did not return any rows.')


with DAG('my_dag', default_args=default_args, schedule_interval='@daily') as dag:
    # Define the BigQueryCheckOperator task
    check_task = BigQueryCheckOperator(
        task_id='check_bq_table',
        sql='SELECT COUNT(*) FROM my_dataset.my_table WHERE created_date = "{{ ds }}"',
        use_legacy_sql=False,
        bigquery_conn_id='my_bigquery_connection',
        dag=dag
    )

    downstream_task = ...
    
    # Define a downstream task to process the output of the BigQueryCheckOperator
    process_task = PythonOperator(
        task_id='process_bq_check',
        python_callable=process_bq_check,
        provide_context=True,
        dag=dag
    )
    

    # Set the dependency between the tasks
    check_task >> process_task >> downstream_task

