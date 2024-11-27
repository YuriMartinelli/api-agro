from flask import Flask
from .database import db, migrate
from app.routes import produtores_route, dashboard_route

def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(produtores_route.bp)
    app.register_blueprint(dashboard_route.bp)

    
    return app
