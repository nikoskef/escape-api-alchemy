from models.room import RoomModel
from tests.integration.integration_base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
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

            self.assertIsNone(RoomModel.find_by_id(1))

            room.save_to_db()

            self.assertIsNotNone(RoomModel.find_by_name_company('Test Name', 'Test Company'))
            self.assertIsNotNone(RoomModel.find_by_id(1))
            self.assertIsNotNone(RoomModel.get_all_rooms())

            room.delete_from_db()

            self.assertIsNone(RoomModel.find_by_id(1))
            self.assertEqual(RoomModel.get_all_rooms(), {'rooms': []})