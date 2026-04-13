from airflow.sdk import dag, task

@dag(
    dag_id="xComDagsManual"
)
def xComDagsManual():
    @task.python
    def firstTask(**kwargs):
        ti = kwargs['ti']
        fetch_data = {"data": [1,2,3,4]}
        ti.xcom_push(key='result1', value=fetch_data)
        
    
    @task.python
    def secondTask(**kwargs):
        ti = kwargs['ti']
        fetch_data = ti.xcom_pull(key='result1', task_ids='firstTask')['data']
        multiply_data = fetch_data*2
        transorm_data = {"transform_data": multiply_data}
        ti.xcom_push(key='result2', value=transorm_data)
    
    @task.python
    def thirdTask(**kwargs):
        ti = kwargs['ti']
        load_data = ti.xcom_pull(key='result2', task_ids='secondTask')
        return load_data
    
    #define task dependency
    first = firstTask()
    second = secondTask()
    third = thirdTask()

    first >> second >> third

#initializing the dag
xComDagsManual()

