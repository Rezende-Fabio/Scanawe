from app import app
from flask import render_template, request

@app.route("/relatorio/lista-relatorios")
def listaRelatorios():
    return render_template("Consultor/listaRelatorios.html", titulo="Listagem de Relatórios")


@app.route("/relatorio/cadastrar-relatorio")
def cadastarRelatorio():
    return render_template("Consultor/cadastrarRelatorio.html", titulo="Gerar Relatório")