from flask import make_response,jsonify,request
from flask import Blueprint
from flask_jwt_extended import create_access_token, set_access_cookies
from database.models.requests.adresseRequest import AdresseRequest
from database.models.requests.userRequest import UserRequest
#from config.conf import IMAGE_PATH_SERVE
from database.services.userServices import UserSerivce
UserController = Blueprint('UserController', __name__)


@UserController.route('/api/register',methods=['POST'])
def register():
    # create adresse request object
    adresseRequest = AdresseRequest(request.get_json())
    # create userRequest object
    userRequest = UserRequest(request.get_json(),adresseRequest)
    userSerivce = UserSerivce(userRequest)
    #
    #   Save the new user into database
    #

    print(userRequest.getEmail())
    user = userSerivce.save()
    if(user == False):
        return make_response(jsonify({"Warn": "Bad Request"}),401)
    res = jsonify({"INFO": "Register Succes"})
    access_token = create_access_token(identity = userSerivce.findById(user))
    set_access_cookies(res,access_token)
    return res,201

@UserController.route('/api/login',methods=['POST'])
def login():
    #? geting user login credentials email and password
    userEmail = request.get_json()['userEmail']
    userPassword = request.get_json()['userPassword']

    #? create userService instance
    userSerivce = UserSerivce()

    #? get user from  database with the same email adresse
    user = userSerivce.findByEmail(userEmail)
    #! check if there is user and check for password after
    if user is not None:
        if user.password == userPassword:
            res = jsonify({"INFO": "Login Succes"})
            access_token = create_access_token(identity = user)
            set_access_cookies(res,access_token)
            return res,201
    return make_response(jsonify({"INFO": "Login Denied"}),401)

@UserController.route('/api/delete/user/:id',methods=['DELETE'])
def deleteUser(id):
    pass




