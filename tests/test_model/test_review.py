#!/usr/bin/python3
"""this is the unittest of review.py"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """this class implement the unittest of the review.py"""
    def test_instance_creation(self):
        """ Test if an instance of Review is created successfully """
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsNotNone(review.id)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)

    def test_attributes(self):
        """ Test if the attributes of Review are present and initialized correctly """
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_to_dict(self):
        """ Test if the to_dict method returns a dictionary representation of Review """
        review = Review()
        review_dict = review.to_dict()

        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['id'], review.id)
        self.assertEqual(review_dict['created_at'], review.created_at.isoformat())
        self.assertEqual(review_dict['updated_at'], review.updated_at.isoformat())
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], review.place_id)
        self.assertEqual(review_dict['user_id'], review.user_id)
        self.assertEqual(review_dict['text'], review.text)

    def test_from_dict(self):
        """ Test if an instance of Review can be created from a dictionary """
        review_data = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T12:34:56',
            '__class__': 'Review',
            'place_id': '456',
            'user_id': '789',
            'text': 'Great experience!'
        }
        review = Review(**review_data)

        self.assertEqual(review.id, '123')
        self.assertEqual(review.created_at.isoformat(), '2022-01-01T00:00:00')
        self.assertEqual(review.updated_at.isoformat(), '2022-01-02T12:34:56')
        self.assertEqual(review.place_id, '456')
        self.assertEqual(review.user_id, '789')
        self.assertEqual(review.text, 'Great experience!')


if __name__ == '__main__':
    unittest.main()
