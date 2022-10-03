#!/usr/bin/python3
"""Test module for state class"""
import unittest
import models.state
from models.state import State


class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in state class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.state.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(State.__doc__), 1)
