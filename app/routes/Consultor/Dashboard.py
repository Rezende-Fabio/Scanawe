from app import app
from flask import render_template, request

@app.route("/dashboard")
def dashboard():
    empresas = "5"
    questionarios = "5"
    relatorios = "2"
    dados = {"empresas": empresas.zfill(3), "questionarios": questionarios.zfill(3), "relatorios": relatorios.zfill(3)}
    return render_template("Consultor/dashboard.html", titulo="Dashboard", dados=dados)