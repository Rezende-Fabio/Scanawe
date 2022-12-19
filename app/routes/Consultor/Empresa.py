from app import app
from flask import render_template, request

@app.route("/empresa/lista-empresas")
def listaEmpresas():
    return render_template("Consultor/listaEmpresas.html", titulo="Listagem de Empresas")


@app.route("/empresa/cadastrar-empresa")
def cadastrarEmpresa():
    return render_template("Consultor/cadastrarEmpresa.html", titulo="Cadastro de Empresas")