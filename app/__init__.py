from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # Get the root directory path
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app = Flask(__name__, template_folder=os.path.join(root_dir, 'templates'), static_folder=os.path.join(root_dir, 'static'))
    
    # Configuration
    app.config['SECRET_KEY'] = 'mehendi-app-secret-key-2024'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mehendi.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Register blueprints
    from app.routes import auth_bp, main_bp, designs_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(designs_bp)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app
