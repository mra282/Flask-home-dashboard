from flask import Flask
from .blueprints.dashboard import dashboard
from .blueprints.api import api
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    app.register_blueprint(dashboard, url_prefix='/dashboard')
    app.register_blueprint(api, url_prefix='/api')

    return app

app = create_app()