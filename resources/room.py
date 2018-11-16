from flask_restful import Resource, reqparse
from models.room import RoomModel
from flask_jwt_extended import jwt_required, get_jwt_claims


class Room(Resource):
    @jwt_required
    def get(self, _id):
        room = RoomModel.find_by_id(_id)
        if room:
            return room.json()
        return {'message': 'Room not Found'}, 404

    @jwt_required
    def delete(self, _id):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401
        parser = reqparse.RequestParser()
        parser.add_argument('company',
                            type=str,
                            required=True,
                            help='You must enter company'
                            )
        parser.add_argument('name',
                            type=str,
                            required=True,
                            help='You must enter a name'
                            )
        data = parser.parse_args()
        room = RoomModel.find_by_name_company(**data)
        if room:
            room.delete_from_db()
            return {'message': 'Room was deleted'}
        return {'message': "No room found with id {}, name '{}' and company '{}'".format(_id, data['name'], data['company'])}, 400


class RoomList(Resource):
    def get(self):
        rooms = RoomModel.get_all_rooms()
        if rooms:
            return rooms
        return {'message': 'No rooms to display'}, 404


class RoomCreate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('company',
                        type=str,
                        required=True,
                        help='You must enter company'
                        )
    parser.add_argument('location',
                        type=str,
                        required=True,
                        help='You must enter a location'
                        )
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='You must enter a name'
                        )
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help='You must enter a description'
                        )
    parser.add_argument('rateofescape',
                        type=str,
                        required=True,
                        help='You must enter a Rate of Escape'
                        )
    parser.add_argument('image',
                        type=str,
                        required=True,
                        help='You must enter an Image'
                        )
    parser.add_argument('duration',
                        type=str,
                        required=True,
                        help='You must enter a Duration'
                        )
    parser.add_argument('playedon',
                        type=str,
                        required=True,
                        help='You must enter a playedon'
                        )

    def post(self):
        data = RoomCreate.parser.parse_args()
        room = RoomModel.find_by_name_company(data['name'], data['company'])
        if room:
            return {'message': "'{}' by '{}' already exists".format(data['name'], data['company'])}, 400

        room = RoomModel(None, **data)

        room.save_to_db()

        return {'message': 'Room Created'}, 201