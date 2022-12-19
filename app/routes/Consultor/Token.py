from app import app
from flask import render_template, request, session


@app.route("/token/gerar-token")
def token():
    return render_template("Consultor/token.html", titulo="Gerar Token")