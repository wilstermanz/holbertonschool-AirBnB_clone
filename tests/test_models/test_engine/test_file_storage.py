#!/usr/bin/python3
import models
from models import storage
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import unittest
from datetime import datetime, time


class TestFileStorageDoc(unittest.TestCase):
    """Contains tests for documentation in base_model"""
    def test_module_doc(self):
        """Checks for documentation in file_storage module"""
        self.assertGreaterEqual(len(file_storage.__doc__), 1)

    def test_class_doc(self):
        """Checks for documentation in FileStorage"""
        self.assertGreaterEqual(len(FileStorage.__doc__), 1)

    def test_all(self):
        """Checks for documentation of the all method"""
        self.assertGreaterEqual(len(FileStorage.all.__doc__), 1)

    def test_new(self):
        """Checks for documentation of the new method"""
        self.assertGreaterEqual(len(FileStorage.new.__doc__), 1)

    def test_save(self):
        """Checks for documentation of the all method"""
        self.assertGreaterEqual(len(FileStorage.save.__doc__), 1)

    def test_reload(self):
        """Checks for documentation of the all method"""
        self.assertGreaterEqual(len(FileStorage.reload.__doc__), 1)


if __name__ == '__main__':
    unittest.main()

# all_objs = storage.all()
# print("-- Reloaded objects --")
# for obj_id in all_objs.keys():
#     obj = all_objs[obj_id]
#     print(obj)

# print("-- Create a new object --")
# my_model = BaseModel()
# my_model.name = "My_First_Model"
# my_model.my_number = 89
# my_model.save()
# print(my_model)
