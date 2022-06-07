from flask import Flask
from flask_cors import CORS
#from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

# LOCAL IMPORTATION
from controllers.userController import UserController
from config.conf import DB_URI, ORIGINS, PRIVATE_KEY
app = Flask(__name__,static_folder='assets')
app.config['JWT_SECRET_KEY'] = PRIVATE_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db = SQLAlchemy(app)


jwt = JWTManager(app)
cors = CORS(app, resources={r"*": {"origins": ORIGINS}},supports_credentials=True)
app.config['SECRET_KEY'] = PRIVATE_KEY
app.register_blueprint(UserController)
#socketio = SocketIO(app)



if __name__ == "__main__":
    #socketio.run(app)
    db.create_all()
    app.run(host='127.0.0.1', port=5000,debug=True)