from app import app
from flask import render_template, request

@app.route("/lista-questionarios")
def listaQuestionarios():
    return render_template("Consultor/listaQuestionarios.html")


@app.route("/cadastrar-questionario")
def cadastarQuestionario():
    return render_template("Consultor/cadastrarQuestionario.html")