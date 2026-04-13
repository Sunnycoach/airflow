from pendulum import datetime
from airflow.sdk import dag,task
from airflow.timetables.interval import CronDataIntervalTimetable

@dag(
        schedule=CronDataIntervalTimetable("@daily", timezone = 'UTC'),
        start_date=datetime(year=2026, month=4, day=1, tz="UTC"),
        end_date = datetime(year=2026, month=4, day=15, tz="UTC"),
        catchup=True
)
def incrementalLoadNew():
    @task.python
    def dataFetch(**kwargs):
        data_interval_start = kwargs['data_interval_start']
        data_interval_end = kwargs['data_interval_end']
        print(f"Fetching data from {data_interval_start}to {data_interval_end}")
    
    @task.bash
    def incrementalProcess():
        return "echo 'Processing incremental data from {{ data_interval_start }} to {{ data_interval_end }}'"
    
    fetch = dataFetch()
    process = incrementalProcess()
    
    fetch >> process

incrementalLoadNew()
