from airflow.sdk import dag, task

@dag(
    dag_id="firstDag"
)
def firstDag():
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
firstDag()

