#!/usr/bin/python3
"""Test module for city class"""
import unittest
import models.city
from models.city import City


class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in city class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.city.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(City.__doc__), 1)
