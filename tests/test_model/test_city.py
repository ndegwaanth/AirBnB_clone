#!/usr/bin/env python3
"""this is the test of the city.py"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """this is the class that implement the the unittest of the city.py"""
    def test_instance_creation(self):
        """ Test if an instance of City is created successfully """
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    def test_attributes(self):
        """ Test if the attributes of City are present and initialized correctly """
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_to_dict(self):
        """ Test if the to_dict method returns a dictionary representation of City """
        city = City()
        city_dict = city.to_dict()

        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['id'], city.id)
        self.assertEqual(city_dict['created_at'], city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'], city.updated_at.isoformat())
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], city.state_id)
        self.assertEqual(city_dict['name'], city.name)

    def test_from_dict(self):
        """ Test if an instance of City can be created from a dictionary"""
        city_data = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T12:34:56',
            '__class__': 'City',
            'state_id': '456',
            'name': 'New York'
        }
        city = City(**city_data)

        self.assertEqual(city.id, '123')
        self.assertEqual(city.created_at.isoformat(), '2022-01-01T00:00:00')
        self.assertEqual(city.updated_at.isoformat(), '2022-01-02T12:34:56')
        self.assertEqual(city.state_id, '456')
        self.assertEqual(city.name, 'New York')

if __name__ == '__main__':
    unittest.main()
