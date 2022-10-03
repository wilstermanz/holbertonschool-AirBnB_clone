#!/usr/bin/python3
"""Test module for place class"""
import unittest
import models.place
from models.place import Place


class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in place class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(models.place.__doc__, 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(Place.__doc__, 1)
