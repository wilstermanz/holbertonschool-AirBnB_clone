#!/usr/bin/python3
"""Test module for review class"""
import unittest
import models.review
from models.review import Review


class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in review class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.review.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(Review.__doc__), 1)
