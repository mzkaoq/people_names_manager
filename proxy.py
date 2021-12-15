from abc import ABC
from flyweight import FlyweightFactory
from serviceInterface import ServiceInterface


class Proxy(ServiceInterface):
    def __init__(self):
        self._factory = FlyweightFactory()

    def add_to_stack(self, data):
        new_names = []
        for name in data[0]:
            new_name = name[0].upper()+name[1:].lower()
            new_names.append(new_name)
        returned_value = self._factory.add_to_stack([new_names,data[1]])
        return returned_value

    def printing(self):
        self._factory.printing()

