from flask import Blueprint
from app.services.customer.customer import Customer
from flask import Flask, render_template

customer_blueprint = Blueprint("customer", __name__, url_prefix="/customer")


@customer_blueprint.route("/", methods=["GET", "POST"])
def hello():
    return "Hello, this is a CUSTOMER API"

@customer_blueprint.route("/hello", methods=["GET", "POST"])
def test_3():
    return "HELLO, this is a CUSTOMER API"

@customer_blueprint.route("/CustomerAnalysis", methods=["GET"])
def get_customer_analysis():
    obj_job_role = Customer()
    plot_url = obj_job_role.get_customer_analysis()
    
    return render_template('analysis.html', plot_url=plot_url)

@customer_blueprint.route("/Customers", methods=["GET"])
def get_all_customer():
    obj_job_role = Customer()
    customer_data = obj_job_role.get_all_customer()
    
    temp = customer_data.to_dict('records')
    columnNames = customer_data.columns.values

    return render_template('record.html', records=temp, colnames=columnNames)