from airflow.sdk import dag, task

@dag(
    dag_id="parallelDag"
)
def parallelDag():
    @task.python
    def extractData(**kwargs):
        ti = kwargs['ti']
        extract_data = {"source1": [1,2,3,4],
                        "source2": [5,6,7,8],
                        "source3": [9,10,11,12]}
        ti.xcom_push(key='return_value', value=extract_data)
    
    @task.python
    def transformTask1(**kwargs):
        ti = kwargs['ti']
        source1 = ti.xcom_pull(task_ids='extractData')['source1']
        transormsource1= [i*2 for i in source1]
        ti.xcom_push(key='return_value',value=transormsource1)
    
    @task.python
    def transformTask2(**kwargs):
        ti = kwargs['ti']
        source2 = ti.xcom_pull(task_ids='extractData')['source2']
        transormsource2= [i*4 for i in source2]
        ti.xcom_push(key='return_value',value=transormsource2)
    
    @task.python
    def transformTask3(**kwargs):
        ti = kwargs['ti']
        source3 = ti.xcom_pull(task_ids='extractData')['source3']
        transormsource3= [i*4 for i in source3]
        ti.xcom_push(key='return_value',value=transormsource3)

    @task.bash
    def loadData(**kwargs):
        print("loading data..........")
        s1 = kwargs['ti'].xcom_pull(task_ids='transformTask1')
        s2 = kwargs['ti'].xcom_pull(task_ids='transformTask2')
        s3 = kwargs['ti'].xcom_pull(task_ids='transformTask3')

        return f"echo 'Load Data: {s1},{s2},{s3}'"

    extract = extractData()
    transform1 = transformTask1()
    transform2 = transformTask2()
    transform3 = transformTask3()
    load = loadData()

    extract >> [transform1,transform2,transform3] >> load


#initializing the dag
parallelDag()

