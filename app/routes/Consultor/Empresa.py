from app import app
from flask import render_template, request

@app.route("/lista-empresas")
def listaEmpresas():
    return render_template("Consultor/listaEmpresas.html")


@app.route("/cadastrar-empresa")
def cadastrarEmpresa():
    return render_template("Consultor/cadastrarEmpresa.html")