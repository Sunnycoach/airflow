from airflow.sdk import dag, task
from pendulum import datetime, duration
from airflow.timetables.trigger import DeltaTriggerTimetable

@dag(
    dag_id="deltaScheduleDag",
    start_date = datetime(year=2026, month=1, day=1, tz="UTC"),
    schedule = DeltaTriggerTimetable(duration(days=3)),
    end_date = datetime(year=2026, month=4, day=16, tz="UTC"),
    is_paused_upon_creation=False,
    catchup=False
)
def deltaScheduleDag():
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
deltaScheduleDag()

