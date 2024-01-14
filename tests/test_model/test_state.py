#!/usr/bin/env python3
"""this implement unittest in state.py"""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    """this class implement the unittest of the state.py"""
    def test_instance_creation(self):
        """ Test if an instance of State is created successfully """
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsNotNone(state.id)
        self.assertIsNotNone(state.created_at)
        self.assertIsNotNone(state.updated_at)

    def test_attributes(self):
        """ Test if the attributes of State are present and initialized correctly """
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_to_dict(self):
        """ Test if the to_dict method returns a dictionary representation of State """
        state = State()
        state_dict = state.do_dict()  # Corrected method name

        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['id'], state.id)
        self.assertEqual(state_dict['created_at'], state.created_at.isoformat())
        self.assertEqual(state_dict['updated_at'], state.updated_at.isoformat())
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], state.name)

    def test_from_dict(self):
        """ Test if an instance of State can be created from a dictionary """
        state_data = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T12:34:56',
            '__class__': 'State',
            'name': 'California'
        }
        state = State(**state_data)

        self.assertEqual(state.id, '123')
        self.assertEqual(state.created_at.isoformat(), '2022-01-01T00:00:00')
        self.assertEqual(state.updated_at.isoformat(), '2022-01-02T12:34:56')
        self.assertEqual(state.name, 'California')

if __name__ == '__main__':
    unittest.main()
