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
        return render_template("index.html", aviso=True)

