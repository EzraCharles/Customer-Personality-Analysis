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
        
    def get_customer_analysis(self):
        ENV = dotenv_values("/home/echarles/Documents/DEV/GitHub/Customer-Personality-Analysis/flask-template/app/.env")
        pickle_file_pca = ENV["PCA"]
        pickle_file_svm = ENV["SVM"]
        pickle_file_kmeans = ENV["KMEANS"]

        df = self.get_all_customer()
        # PCA
        with open(pickle_file_pca,'rb') as file:
            pickle_pca = pickle.load(file)
        cols_when_model_builds = pickle_pca.components_
        df = df[cols_when_model_builds]
        X_PCA = pickle_pca.transform(df)

        # SVM
        with open(pickle_file_svm,'rb') as file:
            pickle_svm = pickle.load(file)
        X_SVM = pickle_svm.predict(X_PCA)
        df['labels'] = X_SVM

        img = io.StringIO.StringIO()
        # plt.plot(df["Spent"], df["Income"])
        fig, ax = plt.subplots(figsize=(5, 5))
        sns.scatterplot(data=df, x="Spent", y="Income", ax=ax, hue="labels")
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)

        plot_url = base64.b64encode(img.getvalue())

        return plot_url