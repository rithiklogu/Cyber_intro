import os
import sys
import json
import pymongo
import certifi
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from Cyber_intro.exception.exception import CyberException
from Cyber_intro.logging.logger import logging

# Load environment variables from .env file
load_dotenv()
MONGO_DB_URL = os.getenv('MONGO_DB_URL')

# Debugging: Print MongoDB URL
print(f"MongoDB URL: {MONGO_DB_URL}")

# Get the certificate for SSL connection
ca = certifi.where()


class CyberDataHandler:
    def __init__(self):
        """
        Initializes MongoDB connection.
        """
        try:
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
        except Exception as e:
            raise CyberException(e, sys)

    def csv_to_json(self, file_path):
        """
        Converts CSV data to JSON format.
        """
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)

            # Convert DataFrame to JSON
            records = json.loads(data.to_json(orient="records"))
            return records
        except Exception as e:
            raise CyberException(e, sys)

    def insert_record(self, records, database, collection):
        """
        Inserts records into MongoDB.
        """
        try:
            db = self.mongo_client[database]  # Select database
            col = db[collection]  # Select collection

            # Insert records into collection
            col.insert_many(records)
            return len(records)
        except Exception as e:
            raise CyberException(e, sys)


if __name__ == '__main__':
    FILE_PATH = r"C:\Users\rithi\Desktop\DS_PRO\Own Pro\ML projects\Cyber_intro\Data\raw_data.csv"
    DATABASE = "CYBER_INTRO"
    COLLECTION = "CyberData"

    # Create an instance of CyberDataHandler        
    cyber_obj = CyberDataHandler()

    # Convert CSV to JSON
    records = cyber_obj.csv_to_json(file_path=FILE_PATH)
    print(f"Converted Records: {records}")

    # Insert data into MongoDB
    no_of_records = cyber_obj.insert_record(records, DATABASE, COLLECTION)
    print(f"Number of records inserted: {no_of_records}")
