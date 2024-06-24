#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage

storage_t = os.getenv('HBNB_TYPE_STORAGE')
print(storage_t)
if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
    from models.engine.db_storage import DBStorage
    storage_t = "db"
    storage = DBStorage()
    storage.reload()
else:
    storage_t = "file"
    storage = FileStorage()
    storage.reload()
