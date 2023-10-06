from flask import Flask
from flask_cors import CORS
from app.routes.customer.controller import customer_blueprint

from dotenv import dotenv_values,load_dotenv

app = Flask(__name__)
CORS(app)

app.register_blueprint(customer_blueprint)

# Environment Variables
ENV = dotenv_values("/home/echarles/Documents/DEV/GitHub/Customer-Personality-Analysis/flask-template/app/.env")
load_dotenv(override=False)
print("Env: ",ENV)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return "hello the services is working"
