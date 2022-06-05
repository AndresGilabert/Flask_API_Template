# load libaries
#   general libraries
from flask import Blueprint, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

import json
import datetime

# define the blueprint
blueprint_v1_auth = Blueprint(name="blueprint_v1_auth", import_name=__name__)


@blueprint_v1_auth.route("/login", methods=['POST'])
def auth_login():
    """
    ---
    post:
      description: Makes login and returns the JWT to autorice the rest of methods
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                email:
                  type: string
                password:
                  type: string
      responses:
        '200':
          description: Call successful
          content:
            application/json:
              schema:
                type: object
                properties:
                  UserName:
                    type: string
                  token:
                    type: string
        '401':
          description: UNAUTHORIZED
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
      tags:
          - Auth
    """
    search_data = json.loads(request.data)
    email = search_data["email"]
    password = search_data["password"]
    intIDUser = 0
    strUserName = ""

    if email == 'test@email.com' & password == 'thisisthepass':
      intIDUser = 951
      strUserName = 'Andres'


    if intIDUser == 0:
        return {'error': 'Email or password invalid'}, 401
    
    expires = datetime.timedelta(days=7)
    access_token = create_access_token(identity=str(intIDUser), expires_delta=expires)
    return {'token': access_token, 'UserName': strUserName}, 200

@blueprint_v1_auth.route("/checkJWT", methods=['GET'])
@jwt_required()
def checkJWT():
    """
    ---
    get:
      description: Check the JWT and return the ID of the user
      responses:
        '200':
          description: Call successful
          content:
            application/json:
              schema:
                type: object
                properties:
                  JWTValid:
                    type: boolean
      tags:
          - Auth
    """
    ## With the decorator @jwt_required, if the JWT is not correct, returns automatically the error
    return {'JWTValid': True}, 200