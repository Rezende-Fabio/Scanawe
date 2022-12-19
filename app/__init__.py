from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'

from app import routes
from app.routes import Main
from app.routes.Consultor import Dashboard, Empresa, Questionario, Relatorio, Token
from app.routes.Gestor import *
