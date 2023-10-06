from app.db.mongodb import MongoDB as mongo
import json
from bson import json_util
import pandas as pd
import pickle
from dotenv import dotenv_values,load_dotenv
# For rendering
import matplotlib 
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

class Customer(mongo):
    
    def __init__(self):
        print("Hi")
        
    def get_all_customer(self):
        ENV = dotenv_values("/home/echarles/Documents/DEV/GitHub/Customer-Personality-Analysis/flask-template/app/.env")
        load_dotenv(override=False)
        data = pd.read_csv(ENV["CUSTOMER_CSV"])
        #customer_dict = self.convert_to_json(data)
        return data
        
    def convert_to_json(self,mongo_reponse):
        # Dump loaded Binary to valid JSON string and reload it as dict
        mongo_dict = json.loads(json_util.dumps(mongo_reponse))
        
        return mongo_dict
        
    def get_customer_analysis(self, group):
        ENV = dotenv_values("/home/echarles/Documents/DEV/GitHub/Customer-Personality-Analysis/flask-template/app/.env")

        df = self.get_all_customer()
        group = df.loc[(df['labels'] == int(group))]

        return group