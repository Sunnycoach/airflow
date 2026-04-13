from airflow.sdk import dag, task

@dag(
    dag_id="xComDagsAuto"
)
def xComDagsAuto():
    @task.python
    def firstTask():
        fetch_date = {"data": [1,2,3,4]}
        return fetch_date
    
    @task.python
    def secondTask(data: dict):
        fetch_data = data['data']
        multiply_data = fetch_data*2
        transorm_data = {"transform_data": multiply_data}
        return transorm_data
    
    @task.python
    def thirdTask(data: dict):
        load_data = data
        return load_data
    
    #define task dependency
    first = firstTask()
    second = secondTask(first)
    third = thirdTask(second)

#initializing the dag
xComDagsAuto()

