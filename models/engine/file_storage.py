#!/usr/bin/python3
"""This module contains the class for file storage"""
import json


class FileStorage:
    """
    This class serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file does not exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                self.__objects = json.loads(file.read())
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
