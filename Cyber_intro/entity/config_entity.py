from  datetime import datetime
import os 
from Cyber_intro.constant import training_pipeline

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.AIRFACT_DIR)

class TrainingPipelineconfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%Y-%m-%d-%H-%M-%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.airtfact_name = training_pipeline.AIRTFACT_DIR
        self.airtfact_dir = os.path.join(self.airfact_dir,timestamp)
        self.timestamp:str = timestamp

    

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineconfig):
        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.airtfact_dir,training_pipeline.DATA_INGESTION_DIR_NAME)