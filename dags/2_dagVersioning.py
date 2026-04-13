from airflow.sdk import dag, task

@dag(
    dag_id="VersionedDag"
)
def versionDag():
    @task.python
    def firstTask():
        print("this is my first task")
    
    @task.python
    def secondTask():
        print("this is my 2nd task")
    
    @task.python
    def thirdTask():
        print("this is my 3rd task")

    @task.python
    def versionTask():
        print("this is my version task")
    
    #define task dependency
    first = firstTask()
    second = secondTask()
    third = thirdTask()
    version = versionTask()

    first >> second >> third >> version

versionDag()

