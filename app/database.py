from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def init_db(app):
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
