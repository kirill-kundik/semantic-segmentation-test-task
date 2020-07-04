from flask import Flask

"""Construct the core application."""
app = Flask(__name__, instance_relative_config=False)
# Application Configuration
app.config.from_object('app.config.Config')


def create_app():
    with app.app_context():
        from app.routes import index, api
        app.register_blueprint(index.index_bp)
        app.register_blueprint(api.api_bp, url_prefix='/api/v1')

        return app
