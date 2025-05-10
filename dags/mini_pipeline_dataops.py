from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    'mini_pipeline_dataops',
    description='Pipeline de ingestão, transformação, carga e consumo de dados COVID-19',
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    ingestao = BashOperator(
        task_id='ingestao',
        bash_command='python3 /Users/antoniomarcos/PycharmProjects/airflow_project/scripts/01_ingestao.py',
    )

    transformacao = BashOperator(
        task_id='transformacao',
        bash_command='python3 /Users/antoniomarcos/PycharmProjects/airflow_project/scripts/02_transformacao.py',
    )

    carga = BashOperator(
        task_id='carga',
        bash_command='python3 /Users/antoniomarcos/PycharmProjects/airflow_project/scripts/03_carga.py',
    )

    consumo = BashOperator(
        task_id='consumo',
        bash_command='python3 /Users/antoniomarcos/PycharmProjects/airflow_project/scripts/04_consumo.py',
    )

    ingestao >> transformacao >> carga >> consumo
