from models.room import RoomModel
from tests.unit.unit_base_test import UnitBaseTest


class RoomTest(UnitBaseTest):
    def test_create_room(self):
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

        self.assertEqual(room.name, 'Test Name',
                         "The name of the room does not equal the constructors argument")
        self.assertEqual(room.location, 'Test Location',
                         "The location of the room does not equal the constructors argument")

    def test_room_json(self):
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
        expected = {
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

        self.assertEqual(room.json(), expected)