import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS

from security import authenticate, identity
from resources.user import UserRegister
from resources.room import Room, RoomList, RoomCreate

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] =os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Room, '/room/<int:_id>')
api.add_resource(RoomCreate, '/room/create')
api.add_resource(RoomList, '/rooms')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)