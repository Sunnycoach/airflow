from pendulum import datetime
from airflow.sdk import dag,task, asset
import os
from a_14_assetsDags import finalDataAsset

@asset(
    schedule=finalDataAsset,
    uri="/opt/airflow/logs/data/final_processed.txt",
    name="dependentDataAsset"
)

def dependentDataAsset(self):
    os.makedirs(os.path.dirname(self.uri), exist_ok=True)
    with open(self.uri, 'w') as f:
        f.write("This is the final data asset content")
    print(f'Data processed succesfully {self.uri}')