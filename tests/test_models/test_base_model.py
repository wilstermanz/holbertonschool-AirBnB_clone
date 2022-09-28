#!/usr/bin/python3
"""Module contains unit tests for the BaseModel class"""
from models import base_model
from models.base_model import BaseModel
import unittest


class TestBaseModelDoc(unittest.TestCase):
    """Contains tests for documentation in base_model"""

    def test_module_doc(self):
        """Checks for documentation in base_model module"""
        self.assertGreaterEqual(len(base_model.__doc__), 1)

    def test_class_doc(self):
        """Checks for documentation in BaseClass"""
        self.assertGreaterEqual(len(BaseModel.__doc__), 1)

    def test_str_doc(self):
        """Checks for documentation of __str__ method"""
        self.assertGreaterEqual(len(BaseModel.__str__.__doc__), 1)

    def test_save_doc(self):
        """Checks for documentation of save() method"""
        self.assertGreaterEqual(len(BaseModel.save.__doc__), 1)

    def test_to_dict_doc(self):
        """Checks for documentation of to_dict() method"""
        self.assertGreaterEqual(len(BaseModel.to_dict.__doc__), 1)


class TestBaseModelAttributes(unittest.TestCase):
    """Checks attributes in BaseModel"""

    def test_id(self):
        """Checks BaseModel.id"""
        o = BaseModel()
        self.assertIsNotNone(o.id)
        o.id = 5
        self.assertEqual(o.id, 5)

    def test_created_at(self):
        """Checks BaseModel.created_at"""
        o = BaseModel()
        self.assertIsNotNone(o.created_at)
        o.created_at = "Now"
        self.assertEqual(o.created_at, "Now")

    def test_updated_at(self):
        """Checks BaseModel.updated_at"""
        o = BaseModel()
        self.assertIsNotNone(o.updated_at)
        o.updated_at = "Now"
        self.assertEqual(o.updated_at, "Now")

    def test_new_attributes(self):
        """Checks added attributes"""
        o = BaseModel()
        o.name = "My First Model"
        o.my_number = 89
        self.assertEqual(o.name, "My First Model")
        self.assertEqual(o.my_number, 89)


# class TestBaseModelMethods(unittest.TestCase):
#     """Checks methods implemented in BaseModel"""

#     def test__init__(self):
#         o = BaseModel()
