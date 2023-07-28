from flask import Flask
from api_livros import bp as bp_api_livros
from controllers.controller_inicial import bp as bp_controller_inicial
from controllers.controller_livros import bp as bp_controller_livros
from controllers.controller_autores import bp as bp_controller_autores


def create_app(test_config=None):
    app = Flask(
        __name__,
        static_url_path = '/static',
        static_folder = 'static',
        instance_relative_config = True
    )

    app.config.from_mapping(
        SECRET_KEY = 'super secret key',
        SESSION_TYPE = 'filesystem',
        JSONIFY_PRETTYPRINT_REGULAR = False
    )

    app.register_blueprint(bp_controller_livros)
    app.register_blueprint(bp_controller_inicial)
    app.register_blueprint(bp_controller_autores)
    app.register_blueprint(bp_api_livros)
    return app

