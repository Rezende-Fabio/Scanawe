from app import app
from flask import render_template, request

@app.route("/dashboard")
def dashboard():
    return render_template("Consultor/dashboard.html", titulo="Dashboard")