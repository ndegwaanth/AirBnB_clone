#!/usr/bin/env python3
"""this is the amenity test"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """this class is base on the amenity test"""
    def test_instance_creation(self):
        """ Test if an instance of Amenity is created successfully """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)

    def test_attributes(self):
        """ Test if the attributes of Amenity are present and initialized correctly """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_to_dict(self):
        """ Test if the to_dict method returns a dictionary representation of Amenity """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()

        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['id'], amenity.id)
        self.assertEqual(amenity_dict['created_at'], amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'], amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], amenity.name)

    def test_from_dict(self):
        """ Test if an instance of Amenity can be created from a dictionary """
        amenity_data = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T12:34:56',
            '__class__': 'Amenity',
            'name': 'Swimming Pool'
        }
        amenity = Amenity(**amenity_data)

        self.assertEqual(amenity.id, '123')
        self.assertEqual(amenity.created_at.isoformat(), '2022-01-01T00:00:00')
        self.assertEqual(amenity.updated_at.isoformat(), '2022-01-02T12:34:56')
        self.assertEqual(amenity.name, 'Swimming Pool')


if __name__ == '__main__':
    unittest.main()
