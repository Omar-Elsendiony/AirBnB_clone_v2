#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls = None):
        """Returns a dictionary of models currently in storage"""
        if (cls is None):
            return FileStorage.__objects
        else:
            objectsToReturn = {}
            for obj_key, obj_val in FileStorage.__objects.items():
                if cls == obj_key.split('.')[0]: # split on the dot and get the first part which is the class name
                    objectsToReturn.update({obj_key:obj_val})
            return objectsToReturn

    

    def delete(self, obj=None):
        """Method to delete a specified object from storage"""
        if (obj is not None):
            key = obj.__class__.__name__ + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()
        
        
    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            try:
                del temp['_sa_instance_state']
                json.dump(temp, f)
            except:
                pass

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                file_content = f.read()
                if file_content:
                    temp = json.loads(file_content)
                    for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
