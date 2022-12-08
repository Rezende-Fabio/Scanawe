from app import app
from flask import render_template, request


@app.route("/token")
def token():
    return render_template("Consultor/token.html")