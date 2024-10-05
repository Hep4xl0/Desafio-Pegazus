from flask import Flask
from src.routes.routes import app as routes_app
from src.helpers.helper import carregar_contas

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Registra as rotas
app.register_blueprint(routes_app)

# Carrega as contas do arquivo JSON quando a aplicação inicia
carregar_contas()

if __name__ == '__main__':
    app.run()
