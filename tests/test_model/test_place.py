#!/usr/bin/env python3
"""this test the place.py file"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """this id the class based on testing the place.py"""
    def test_instance_creation(self):
        """ Test if an instance of Place is created successfully """
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsNotNone(place.id)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)

    def test_attributes(self):
        """ Test if the attributes of Place are present and initialized correctly """
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

        self.assertEqual(place.city_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_to_dict(self):
        """ Test if the to_dict method returns a dictionary representation of Place """
        place = Place()
        place_dict = place.to_dict()

        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['id'], place.id)
        self.assertEqual(place_dict['created_at'], place.created_at.isoformat())
        self.assertEqual(place_dict['updated_at'], place.updated_at.isoformat())
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['city_id'], place.city_id)
        self.assertEqual(place_dict['name'], place.name)
        self.assertEqual(place_dict['description'], place.description)
        self.assertEqual(place_dict['number_rooms'], place.number_rooms)
        self.assertEqual(place_dict['number_bathrooms'], place.number_bathrooms)
        self.assertEqual(place_dict['max_guest'], place.max_guest)
        self.assertEqual(place_dict['price_by_night'], place.price_by_night)
        self.assertEqual(place_dict['latitude'], place.latitude)
        self.assertEqual(place_dict['longitude'], place.longitude)
        self.assertEqual(place_dict['amenity_ids'], place.amenity_ids)

    def test_from_dict(self):
        """ Test if an instance of Place can be created from a dictionary """
        place_data = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T12:34:56',
            '__class__': 'Place',
            'city_id': '456',
            'name': 'Cozy Apartment',
            'description': 'A comfortable place to stay',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'amenity_ids': ['789', '101']
        }
        place = Place(**place_data)

        self.assertEqual(place.id, '123')
        self.assertEqual(place.created_at.isoformat(), '2022-01-01T00:00:00')
        self.assertEqual(place.updated_at.isoformat(), '2022-01-02T12:34:56')
        self.assertEqual(place.city_id, '456')
        self.assertEqual(place.name, 'Cozy Apartment')
        self.assertEqual(place.description, 'A comfortable place to stay')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ['789', '101'])

    def test_instance_creation(self):
        """ Test if an instance of Place is created successfully """
        place1 = Place()
        place2 = Place()

        self.assertIsInstance(place1, Place)
        self.assertIsInstance(place2, Place)

        # Check if each instance has a unique ID
        self.assertNotEqual(place1.id, place2.id)

        self.assertIsNotNone(place1.id)
        self.assertIsNotNone(place2.id)
        self.assertIsNotNone(place1.created_at)
        self.assertIsNotNone(place2.created_at)
        self.assertIsNotNone(place1.updated_at)
        self.assertIsNotNone(place2.updated_at)

    def test_from_dict(self):
        """ Test if an instance of Place can be created from a dictionary """
        place_data = {
            'id': '123',  # Provided ID in kwargs
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T12:34:56',
            '__class__': 'Place',
            'city_id': '456',
            'name': 'Cozy Apartment',
            'description': 'A comfortable place to stay',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'amenity_ids': ['789', '101']
        }
        place = Place(**place_data)

        # Check if provided id and generated id are consistent
        self.assertEqual(place.id, '123')

        self.assertEqual(place.created_at.isoformat(), '2022-01-01T00:00:00')
        self.assertEqual(place.updated_at.isoformat(), '2022-01-02T12:34:56')
        self.assertEqual(place.city_id, '456')
        self.assertEqual(place.name, 'Cozy Apartment')
        self.assertEqual(place.description, 'A comfortable place to stay')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ['789', '101'])


if __name__ == '__main__':
    unittest.main()
