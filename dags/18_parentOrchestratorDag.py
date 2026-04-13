from child_16_orchestrateDag1 import firstOrchestrateDag
from child_17_orchestrateDag2 import secondOrchestrateDag
from airflow.sdk import dag, task
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

@dag(
    dag_id="parentOrchestratorDag"
)
def parentOrchestratorDag():

    triggeFirstDag = TriggerDagRunOperator(
        task_id="trigger_firstOrchestrateDag",
        trigger_dag_id="firstOrchestrateDag",
        wait_for_completion=True
    )

    triggeSecondDag = TriggerDagRunOperator(
        task_id="trigger_secondOrchestrateDag",
        trigger_dag_id="secondOrchestrateDag"
    )
    

    triggeFirstDag >> triggeSecondDag

parentOrchestratorDag()
