from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.routes import produtores

# Instância do banco de dados
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Carregar as configurações
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(produtores.bp)


    return app
