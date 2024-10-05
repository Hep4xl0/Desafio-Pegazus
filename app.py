from flask import Flask
from src.routes.routes import app as routes_app
from src.helpers.helper import carregar_contas

# Create the Flask app
app = Flask(__name__)

# Register the routes blueprint
app.register_blueprint(routes_app)

# Load accounts from JSON at startup
carregar_contas()

if __name__ == '__main__':
    app.run()
