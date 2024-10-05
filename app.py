from flask import Flask
from src.routes.routes import app as routes_app
from src.helpers.helper import carregar_contas

#Cria o app flask para ser usado pelas rotas
app = Flask(__name__)

# REgistra as rotas do flask
app.register_blueprint(routes_app)

#carrega as contas 
carregar_contas()

if __name__ == '__main__':
    app.run()
