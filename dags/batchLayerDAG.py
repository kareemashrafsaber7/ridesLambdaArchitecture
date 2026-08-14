from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator


with DAG(
    dag_id="lambda_batch_pipeline",
    start_date=datetime(2026, 8, 1),
    schedule="0 /12 * * *",
    catchup=False,
    tags=["lambda", "dbt", "databricks", "synapse"],
) as dag:

    dbt_silver = BashOperator(
        task_id="dbt_silver",
        bash_command="cd ridesLambda/batchLayer/silverGoldDBT/dbtLambda/lambdaBatchSG && dbt run --select rides_silver_batch",
    )

    dbt_snapshots = BashOperator(
        task_id="dbt_snapshots",
        bash_command="cd ridesLambda/batchLayer/silverGoldDBT/dbtLambda/lambdaBatchSG && dbt snapshot",
    )

    dbt_gold = BashOperator(
        task_id="dbt_gold",
        bash_command="cd ridesLambda/batchLayer/silverGoldDBT/dbtLambda/lambdaBatchSG && dbt run --select dim_cancellation_reason dim_city dim_payment_methods dim_ride_status dim_vehicle_make dim_vehicle_type dim_driver dim_passenger dim_vehicle fact_rides_batch",
    )

    load_to_synapse = DatabricksRunNowOperator(
        task_id="load_to_synapse",
        databricks_conn_id="",
        job_id=83024790158485,
    )

    dbt_silver >> dbt_snapshots >> dbt_gold >> load_to_synapse