from app import app, render_template, request

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/autenticar", methods=["POST"])
def autenticar():
    usuario = request.form['user']
    senha = request.form["senha"]
    if usuario == "admin" and senha == "admin":
        return render_template("menu.html")
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


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/token")
def token():
    return render_template("token.html")


@app.route("/lista-empresas")
def listaEmpresas():
    return render_template("listaEmpresas.html")


@app.route("/cadastrar-empresa")
def cadastrarEmpresa():
    return render_template("cadastrarEmpresa.html")


@app.route("/lista-relatorios")
def listaRelatorios():
    return render_template("listaRelatorios.html")


@app.route("/cadastrar-relatorio")
def cadastarRelatorio():
    return render_template("cadastrarRelatorio.html")


@app.route("/lista-questionarios")
def listaQuestionarios():
    return render_template("listaQuestionarios.html")


@app.route("/cadastrar-questionario")
def cadastarQuestionario():
    return render_template("cadastrarQuestionario.html")