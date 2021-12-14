from abc import ABC
from flyweight import FlyweightFactory
from serviceInterface import ServiceInterface


class Proxy(ServiceInterface):
    def __init__(self):
        self._factory = FlyweightFactory()

    def add_to_stack(self, data):
        self._factory.add_to_stack(data)

    def printing(self):
        self._factory.printing(self._factory.tree, 1)

    """
    def add_to_stack(self, data):
        for index in range(len(data[0])):
            if index < len(data[0]) - 1:
                self._factory.add_to_stack(data[0][index], "")
                print(data[0][index], "")
            elif index == len(data[0]) - 1:
                self._factory.add_to_stack(data[0][index], data[1])
                print(data[0][index], data[1])
    """
