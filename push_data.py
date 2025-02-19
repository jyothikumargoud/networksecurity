import os
import sys
from dotenv import load_dotenv
import json
# Load the .env file
load_dotenv()
# Fetch MongoDB URL
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
# Debug: Print the variable
print(f"MONGO_DB_URL from os.getenv: {MONGO_DB_URL}")

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from network_security.exception.exception import NetworkSecurityException
from network_security.logging import logger



# Building A simple ETL pipeline to Load the Data into mongodb in the form of json filr format

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json_convorter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)  # this step is going to remove the indexes from dataset since we are stroing in database
            records = list(json.loads(data.T.to_json()).values()) # list of json arrays
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_into_database(self, collection, records, database):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
        
            self.collection = self.database[self.collection]  # Fix: Access collection correctly
            self.collection.insert_many(self.records)
        
            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e,sys)


if __name__ == '__main__':
    FILE_PATH = "/Users/jyothikumargoud/Documents/projects/Networksecurity/Network_data/phisingData.csv"
    DATABASE = "JYOTHI"
    Collection = "NetworkData"
    
    network_obj = NetworkDataExtract()
    records = network_obj.csv_to_json_convorter(file_path=FILE_PATH)
    
    print(records)
    
    no_of_records = network_obj.insert_data_into_database(Collection, records, DATABASE) 
    
    print(no_of_records)


