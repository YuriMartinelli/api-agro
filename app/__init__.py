from flask import Flask
from .database import db, migrate
from app.routes import produtores_route

def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(produtores_route.bp)

    return app
