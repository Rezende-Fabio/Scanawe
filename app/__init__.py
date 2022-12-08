from flask import Flask
app = Flask(__name__)
from app import routes
from app.routes import Main
from app.routes.Consultor import Dashboard, Empresa, Questionario, Relatorio, Token
from app.routes.Gestor import *
