"""Flask Application"""

# load libaries
from flask import Flask, jsonify
from flask_cors import CORS #, cross_origin
from flask_jwt_extended import JWTManager, jwt_required
import sys

# load modules
from src.blueprint.v1.auth import blueprint_v1_auth
from src.blueprint.swagger import swagger_ui_blueprint, SWAGGER_URL

# init Flask app
app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET_KEY'] = '##PUT_YOUR_SECRET_KEY##'

jwt = JWTManager(app)

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(blueprint_v1_auth, url_prefix="/api/v1/auth")
# app.register_blueprint(blueprint_y, url_prefix="/api/v1/path_for_blueprint_y")

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

from src.api_spec import spec

with app.test_request_context():
    # register all swagger documented functions here
    for fn_name in app.view_functions:
        if fn_name == 'static':
            continue
        print(f"Loading swagger docs for function: {fn_name}")
        view_fn = app.view_functions[fn_name]
        spec.path(view=view_fn)

@app.route("/api/swagger.json")
def create_swagger_spec():
    return jsonify(spec.to_dict())