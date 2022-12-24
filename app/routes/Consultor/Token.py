from app import app
from flask import render_template, request, session


@app.route("/token/gerar-token")
@app.route("/token/gerar-token-modal")
def token():
    if "modal" in request.url:
        return render_template("Consultor/token.html", titulo="Gerar Token", aviso=1)
    return render_template("Consultor/token.html", titulo="Gerar Token")