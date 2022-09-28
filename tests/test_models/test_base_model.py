#!/usr/bin/python3
"""Module contains unit tests for the BaseModel class"""
from lib2to3.pytree import Base
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

    def test_init_doc(self):
        """Checks for documentation of __init__ method"""
        self.assertGreaterEqual(len(BaseModel.__init__.__doc__), 1)

    def test_str_doc(self):
        """Checks for documentation of __str__ method"""
        self.assertGreaterEqual(len(BaseModel.__str__.__doc__), 1)

    def test_save_doc(self):
        """Checks for documentation of save() method"""
        self.assertGreaterEqual(len(BaseModel.save.__doc__), 1)

    def test_to_dict_doc(self):
        """Checks for documentation of to_dict() method"""
        self.assertGreaterEqual(len(BaseModel.to_dict.__doc__), 1)


class TestBaseModel(unittest.TestCase):
    """Checks creating model"""
    
    def test_normal(self):
        """Checks that an object is created"""
        o = BaseModel()
        self.assertIsNotNone(o)


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

class TestBaseModelCreateTwo(unittest.TestCase):
    def test_create_two(self):
        """Checks proper function when creating two BaseModels"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertTrue(hasattr(bm2, "id"))
        self.assertTrue(hasattr(bm2, "created_at"))
        self.assertTrue(hasattr(bm2, "updated_at"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertNotEqual(bm1.created_at, bm2.created_at)
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm1.created_at, object)
        self.assertIsInstance(bm1.updated_at, object)
        self.assertIsInstance(bm2.id, str)
        self.assertIsInstance(bm2.created_at, object)
        self.assertIsInstance(bm2.updated_at, object)


class TestBaseModelMethods(unittest.TestCase):
    """Checks methods implemented in BaseModel"""

    def test__str__(self):
        """Checks __str__() method"""
        o = BaseModel()
        self.assertEqual(o.__str__(), (f"[{o.__class__.__name__}] "
                                       f"({o.id}) {o.__dict__}"))

    def test_save(self):
        """Checks save() method"""
        o = BaseModel()
        before_update = o.updated_at
        o.save()
        after_update = o.updated_at
        self.assertNotEqual(before_update, after_update)

    def test_to_dict(self):
        """Checks to_dict() method"""
        o = BaseModel()
        self.assertIsInstance(o.to_dict(), dict)
