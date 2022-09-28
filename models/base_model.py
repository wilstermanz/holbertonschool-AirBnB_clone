#!/usr/bin/python3
"""
base_model module for the AirBnB console project
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel class containing:
    Public id attribute
    Public created_at attribute
    Public updated_at attribute
    __str__ overwrite to print [<class name>] (<self.id>) <self.__dict__>
    Public method save(self)
    Public method to_dict(self)
    """
    def __init__(self, id=None, created_at=None, uupdated_at=None):
        """
        Instantiate public attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Override the string to print [<class name>] (<self.id>) <self.__dict__>
        """
        return("[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__))
