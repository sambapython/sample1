from flask import Flask, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("db1://127.0.0.1:27017") #host uri  
db = client.db1    #Select the database  
customers = db.customer

@app.route("/")
def home():
	"""
	"""
	return render_template("home.html",data=customers)
@app.route("/cust_create/")
def cust_create():
	return render_template("cust_create.html")

if __name__ == "__main__":
	app.run(debug=True)