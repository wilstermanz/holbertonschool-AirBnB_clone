#!/usr/bin/python3
"""Test module for amenity class"""
import unittest
import models.amenity
from models.amenity import Amenity


class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in amenity class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(models.amenity.__doc__, 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(Amenity.__doc__, 1)
