from pendulum import datetime
from airflow.sdk import dag,task
from airflow.timetables.events import EventsTimetable

dates = EventsTimetable(event_dates=[
    datetime(2026,4,4),
    datetime(2026,7,29),
    datetime(2026,12,26)
])

@dag(
        schedule=dates,
        start_date=datetime(year=2026, month=4, day=1, tz="UTC"),
        end_date = datetime(year=2026, month=4, day=15, tz="UTC"),
        is_paused_upon_creation=False,
        catchup=True
)
def specialDags():

    @task.python
    def dataFetch(**kwargs):
        executionDate = kwargs['logical_date']
        print(f"Fetching data for {executionDate}")
    
    process = dataFetch()

specialDags()
