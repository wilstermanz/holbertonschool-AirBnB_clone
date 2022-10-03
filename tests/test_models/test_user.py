#!/usr/bin/python3
"""Test module for user class"""
import unittest
import models.user
from models.user import User


class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in user class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.user.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(User.__doc__), 1)
