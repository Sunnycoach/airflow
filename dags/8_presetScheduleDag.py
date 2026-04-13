from airflow.sdk import dag, task
from pendulum import datetime

@dag(
    dag_id="firstScheduleDag",
    start_date = datetime(year=2026, month=1, day=1, tz="UTC"),
    schedule = "@daily",
    is_paused_upon_creation=False
)
def firstScheduleDag():
    @task.python
    def firstTask():
        print("this is my first task")
    
    @task.python
    def secondTask():
        print("this is my 2nd task")
    
    @task.python
    def thirdTask():
        print("this is my 3rd task")
    
    #define task dependency
    first = firstTask()
    second = secondTask()
    third = thirdTask()

    first >> second >> third

#initializing the dag
firstScheduleDag()

