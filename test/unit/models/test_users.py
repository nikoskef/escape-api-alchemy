from models.user import UserModel
from test.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('username', 'password')

        self.assertEqual(user.username, 'username')
        self.assertEqual(user.password, 'password')
