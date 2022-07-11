#!/usr/bin/python3
import json
"""module contains class Base"""


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instances
        Args:
            - id: id of Base instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            ify = "[]"
        else:
            ify = cls.to_json_string([j.to_dictionary() for j in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(ify)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        my_result = []
        with open(filename, mode='r') as classFile:
            data = classFile.read()

        data = cls.from_json_string(data)
        for item in data:
            if type(item) == dict:
                my_result.append(cls.create(**item))
            else:
                my_result.append(item)
        return my_result
