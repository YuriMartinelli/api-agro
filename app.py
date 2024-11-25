import os
from flask import Flask
from app.database import init_db
from app.routes import produtores
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__)

    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar o banco de dados
    init_db(app)

    # Registrar rotas
    app.register_blueprint(produtores.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
