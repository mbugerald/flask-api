# Global imports
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_wtf.csrf import CSRFProtect, CSRFError
from app.config import base_config
from flask_cors import CORS


# Application Object.
class Application(object):
    # Global variables
    app = Flask(__name__)
    # Associating config file
    app.config.from_object(base_config)
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    csrf = CSRFProtect(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    def __int__(self, app, db, ma, csrf):
        self.app = app
        self.db = db
        self.ma = ma
        self.csrf = csrf
        self.csrf.init_app(self.app)

    # Importing blueprints.
    def import_blue_prints(self):
        # Importing blueprints
        from app.api.route import api
        # Register blueprints.
        self.app.register_blueprint(api)

    @app.errorhandler(404)
    def not_found(self):
        return jsonify({"state": 0,
                        "response": "You haven\'t given me any pointer,"
                        " you then have null results. Either way check your code for "
                        "bugs and error fix."})

