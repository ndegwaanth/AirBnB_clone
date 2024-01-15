#!/usr/bin/env python3
"""this implement a test of user.py"""


import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ this class implement all the test cases of the user.py """
    def test_instance_creation(self):
        """ Test if an instance of User is created successfully """
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    def test_attributes(self):
        """ Test if the attributes of User are present and initialized correctly """
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_to_dict(self):
        """ Test if the to_dict method returns a dictionary representation of User """
        user = User()
        user_dict = user.do_dict()  # Corrected method name

        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['id'], user.id)
        self.assertEqual(user_dict['created_at'], user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'], user.updated_at.isoformat())
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], user.email)
        self.assertEqual(user_dict['password'], user.password)
        self.assertEqual(user_dict['first_name'], user.first_name)
        self.assertEqual(user_dict['last_name'], user.last_name)

    def test_from_dict(self):
        """ Test if an instance of User can be created from a dictionary """
        user_data = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T12:34:56',
            '__class__': 'User',
            'email': 'user@example.com',
            'password': 'secure_password',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User(**user_data)

        self.assertEqual(user.id, '123')
        self.assertEqual(user.created_at.isoformat(), '2022-01-01T00:00:00')
        self.assertEqual(user.updated_at.isoformat(), '2022-01-02T12:34:56')
        self.assertEqual(user.email, 'user@example.com')
        self.assertEqual(user.password, 'secure_password')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_str_representation(self):
        """ Test if the __str__ method returns a string representation of User """
        user = User()
        user_str = str(user)

        self.assertIsInstance(user_str, str)
        self.assertIn("[User] ({})".format(user.id), user_str)


if __name__ == '__main__':
    unittest.main()
