import os 
import sys
import numpy as np
import pandas as pd

""" defining common constant varable for training pipeline"""
TARGET_COLUMN:str= "class"
PIPELINE_NAME:str= "Cyber_intro"
AIRTIFCT_DIR:str ="Airtifacts"
FILE_NAME:str = 'raw_data.csv'

TRAINING_FILE_NAME:str ="train.csv"
TESTING_FILE_NAME:str ="test.csv"

""" Data ingestion related constant start with DATA_INGESTION VAR NAME"""

DATA_INGESTION_DATABASE_NAME: = "CYBER_INTRO"
DATA_INGESTION_COLLECTION_NAME: = "cyber_data"
DATA_INGESTION_DIR_NAME: = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: = "feature_store"
DATA_INGESTION_INGESTED_DIR :srt = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO : float = 0.2



