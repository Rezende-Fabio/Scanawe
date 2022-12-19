from app import app
from flask import render_template, request

@app.route("/questionario/lista-questionarios")
def listaQuestionarios():
    return render_template("Consultor/listaQuestionarios.html", titulo="Listagem de Questionários")


@app.route("/questionario/cadastrar-questionario")
def cadastarQuestionario():
    return render_template("Consultor/cadastrarQuestionario.html", titulo="Cadastrar Questionário")