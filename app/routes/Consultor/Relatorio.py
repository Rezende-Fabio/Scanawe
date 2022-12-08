from app import app
from flask import render_template, request

@app.route("/lista-relatorios")
def listaRelatorios():
    return render_template("Consultor/listaRelatorios.html")


@app.route("/cadastrar-relatorio")
def cadastarRelatorio():
    return render_template("Consultor/cadastrarRelatorio.html")