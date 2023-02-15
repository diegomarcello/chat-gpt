from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryCheckOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 3, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'bigquery_data_quality_check',
    default_args=default_args,
    schedule_interval='0 0 * * *'
)

table_name = 'my_dataset.my_table'

# Define data quality checks for the BigQuery table
checks = [
    {'check_name': 'row_count', 'sql': f'SELECT COUNT(*) FROM `{table_name}`', 'expected_result': 1000},
    {'check_name': 'null_check', 'sql': f'SELECT COUNT(*) FROM `{table_name}` WHERE column1 IS NULL', 'expected_result': 0},
    {'check_name': 'unique_check', 'sql': f'SELECT COUNT(DISTINCT column1) FROM `{table_name}`', 'expected_result': 100},
    # Add additional checks as needed
]

# Create BigQueryCheckOperator for each data quality check
for check in checks:
    task = BigQueryCheckOperator(
        task_id=f'check_{check["check_name"]}',
        sql=check['sql'],
        use_legacy_sql=False,
        expected_result=check['expected_result'],
        location='us-central1',
        bigquery_conn_id='my_gcp_connection',
        dag=dag
    )