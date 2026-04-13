from airflow.sdk import dag, task
from pendulum import datetime
from airflow.timetables.trigger import CronTriggerTimetable

@dag(
    dag_id="cronScheduleDag",
    start_date = datetime(year=2026, month=1, day=1, tz="UTC"),
    schedule = CronTriggerTimetable("0 13 * * MON-FRI", timezone="UTC"),
    end_date = datetime(year=2026, month=4, day=16, tz="UTC"),
    is_paused_upon_creation=False,
    catchup=True
)
def cronScheduleDag():
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
cronScheduleDag()

