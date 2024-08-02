from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Basic Configurations
    app.config['SECRET_KEY'] = 'AkCTR2LP'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cloudflask_manager.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
