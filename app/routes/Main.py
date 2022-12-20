from app import app
from flask import render_template, request, session

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/autenticar", methods=["POST"])
def autenticar():
    usuario = request.form['user']
    senha = request.form["senha"]
    if usuario == "admin" and senha == "admin":
        session["username"] = "Administrador"
        empresas = "5"
        questionarios = "5"
        relatorios = "2"
        dados = {"empresas": empresas.zfill(3), "questionarios": questionarios.zfill(3), "relatorios": relatorios.zfill(3)}
        return render_template("Consultor/dashboard.html", titulo="Dashboard", dados=dados)
    else:
        return render_template("index.html", aviso=1)

@app.route("/esqueci-senha")
def esqueciSenha():
    return render_template("index.html", aviso=2)

@app.route("/esqueciSenha", methods=["POST"])
def esqueciSenhaa():
    with open("teste.txt", "a+") as txt:
        email = request.form["email"]
        usuario = request.form["usuario"]
        txt.write(f"{email}\n{usuario}")
    return render_template("index.html")
