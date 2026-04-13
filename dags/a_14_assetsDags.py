from pendulum import datetime
from airflow.sdk import dag,task, asset
import os

@asset(
    schedule="@daily",
    uri="/opt/airflow/logs/data/final.txt",
    name="finalDataAsset"
)

def finalDataAsset(self):
    print("This is my final data asset")
    os.makedirs(os.path.dirname(self.uri), exist_ok=True)
    with open(self.uri, 'w') as f:
        f.write("This is the final data asset content")
    print(f"data written to {self.uri}")