from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.google.cloud.operators.ai_platform import (
    CreateFeaturestoreOperator,
    ImportFeatureValuesOperator,
    DeleteFeaturestoreOperator,
)
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 3, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'load_data_into_featurestore',
    default_args=default_args,
    description='A DAG to load data into a feature store in Vertex',
    schedule_interval=timedelta(days=1),
)

create_featurestore = CreateFeaturestoreOperator(
    task_id='create_featurestore',
    location='us-central1',
    featurestore_id='my-featurestore',
    dag=dag
)

import_feature_values = ImportFeatureValuesOperator(
    task_id='import_feature_values',
    project_id='my-project',
    location='us-central1',
    featurestore_id='my-featurestore',
    entity_type_id='my-entity-type',
    bigquery_source='my-project:my_dataset.my_table',
    dag=dag,
)

delete_featurestore = DeleteFeaturestoreOperator(
    task_id='delete_featurestore',
    location='us-central1',
    featurestore_id='my-featurestore',
    dag=dag
)

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> create_featurestore >> import_feature_values >> delete_featurestore >> end
