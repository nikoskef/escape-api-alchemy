from models.user import UserModel
from tests.integration.integration_base_test import BaseTest


class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('test', 'abcd')

            self.assertIsNone(UserModel.find_by_username('test'),
                              "A user was found by username wheres it should be none")
            self.assertIsNone(UserModel.find_by_id(1), "A user was found by id wheres it should be none")

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test'), "No users found by username")
            self.assertIsNotNone(UserModel.find_by_id(1), "No users found by id")