from airflow.sdk import dag, task
from airflow.operators.bash import BashOperator

@dag(
    dag_id="bashOperatorDag"
)
def bashOperatorDag():
    @task.python
    def firstTask():
        print("this is my first task")
    
    @task.bash
    def bashTaskModern() -> str:
        return "echo https://airflow.apache.org/"
    
    baskTaskOld = BashOperator(
    task_id="baskTaskOld",
    bash_command="echo https://airflow.apache.org/"
    )
    
    #define task dependency
    first = firstTask()
    second = bashTaskModern()
    third = baskTaskOld

    first >> second >> third

bashOperatorDag()

