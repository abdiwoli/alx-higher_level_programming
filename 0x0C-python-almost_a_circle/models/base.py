#!/usr/bin/python3
"""file"""
import json
import csv
import turtle


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ls = [obj.to_dictionary() for obj in list_objs if obj is not None]
        with open(f"{cls.__name__}.json", "w") as file:
            file.write(cls.to_json_string(ls))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if list_objs:
                fn = list(list_objs[0].to_dictionary().keys())
                writer.writerow(fn)
                for obj in list_objs:
                    if obj is not None:
                        writer.writerow([getattr(obj, field) for field in fn])

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                instances = []
                for row in reader:
                    for key, value in row.items():
                        instances.append(cls.create(**{key: value}))
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in list_dicts]
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.title("Turtle Drawing")
        screen.bgcolor("white")
        pen = turtle.Turtle()
        pen.speed(2)
        for rec in list_rectangles:
            pen.penup()
            pen.goto(rec.x, rec.y)
            pen.pendown()
            for i in range(2):
                pen.forward(rec.width)
                pen.left(90)
                pen.forward(rec.height)
                pen.left(90)
        for sq in list_squares:
            sq.display()
            pen.penup()
            pen.goto(sq.x, sq.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(sq.size)
                pen.right(90)
        turtle.mainloop()
