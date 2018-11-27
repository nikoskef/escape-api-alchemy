from models.room import RoomModel
from models.user import UserModel
from tests.base_test import BaseTest
import json


class RoomTest(BaseTest):
    def setUp(self):
        super(RoomTest, self).setUp()
        with self.app() as client:
            with self.app_context():
                UserModel('test', '1234').save_to_db()
                login_request = client.post('/login',
                                            data=json.dumps({'username': 'test', 'password': '1234'}),
                                            headers={'Content-Type': 'application/json'})
                auth_token = json.loads(login_request.data)['access_token']
                self.access_token = 'Bearer ' + auth_token

    def test_get_room_no_auth(self):
        with self.app() as client:
            with self.app_context():
                request = client.get('/room/1')
                self.assertEqual(request.status_code, 401)

    def test_get_room_not_found(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get('/room/1', headers={'Authorization': self.access_token})
                self.assertEqual(resp.status_code, 404)

    def test_get_room(self):
        with self.app() as client:
            with self.app_context():
                room = RoomModel(
                    _id=1,
                    company='Test Company',
                    location='Test Location',
                    name='Test Name',
                    description='Some Test Description',
                    rateofescape='10/10',
                    image='test.jpg',
                    duration='60 minutes',
                    playedon='01/01/2018'
                )
                room.save_to_db()
                resp = client.get('/room/1', headers={'Authorization': self.access_token})
                self.assertEqual(resp.status_code, 200)

    def test_delete_room(self):
        with self.app() as client:
            with self.app_context():
                room = RoomModel(
                    _id=1,
                    company='Test Company',
                    location='Test Location',
                    name='Test Name',
                    description='Some Test Description',
                    rateofescape='10/10',
                    image='test.jpg',
                    duration='60 minutes',
                    playedon='01/01/2018'
                )
                room.save_to_db()

                resp = client.delete('/room/1',
                                     data={'name': 'Test Name', 'company': 'Test Company'},
                                     headers={'Authorization': self.access_token})
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({'message': 'Room was deleted'}, json.loads(resp.data))

    def test_create_room(self):
        data = {
            'id': 1,
            'company': 'Test Company',
            'location': 'Test Location',
            'name': 'Test Name',
            'description': 'Some Test Description',
            'rateofescape': '10/10',
            'image': 'test.jpg',
            'duration': '60 minutes',
            'playedon': '01/01/2018'
        }

        with self.app() as client:
            with self.app_context():
                resp = client.post('/room/create', data=data)

                self.assertEqual(resp.status_code, 201)
                self.assertDictEqual({'message': 'Room Created'}, json.loads(resp.data))

    def test_create_duplicate_room(self):
        room = RoomModel(
            _id=1,
            company='Test Company',
            location='Test Location',
            name='Test Name',
            description='Some Test Description',
            rateofescape='10/10',
            image='test.jpg',
            duration='60 minutes',
            playedon='01/01/2018'
        )

        data = {
            'id': 1,
            'company': 'Test Company',
            'location': 'Test Location',
            'name': 'Test Name',
            'description': 'Some Test Description',
            'rateofescape': '10/10',
            'image': 'test.jpg',
            'duration': '60 minutes',
            'playedon': '01/01/2018'
        }

        with self.app() as client:
            with self.app_context():
                room.save_to_db()
                resp = client.post('/room/create', data=data)

                self.assertEqual(resp.status_code, 400)
                self.assertDictEqual({'message': "'Test Name' by 'Test Company' already exists"}, json.loads(resp.data))

    def test_room_list(self):
        with self.app() as client:
            with self.app_context():
                room = RoomModel(
                    _id=1,
                    company='Test Company',
                    location='Test Location',
                    name='Test Name',
                    description='Some Test Description',
                    rateofescape='10/10',
                    image='test.jpg',
                    duration='60 minutes',
                    playedon='01/01/2018'
                )
                data = {
                    'id': 1,
                    'company': 'Test Company',
                    'location': 'Test Location',
                    'name': 'Test Name',
                    'description': 'Some Test Description',
                    'rateofescape': '10/10',
                    'image': 'test.jpg',
                    'duration': '60 minutes',
                    'playedon': '01/01/2018'
                }
                room.save_to_db()

                resp = client.get('/rooms')

                self.assertDictEqual({'rooms': [data]}, json.loads(resp.data))
