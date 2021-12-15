from serviceInterface import ServiceInterface


class FlyweightFactory(ServiceInterface):
    def __init__(self):
        self._flyweight_list = []

    def add_to_stack(self, valid_data):
        names = []
        for name in valid_data[0]:
            returned_value = self.name_exists(name)
            if returned_value == False:
                new_object = Flyweight(name)
                self._flyweight_list.append(new_object)
                names.append(new_object)
            else:
                names.append(returned_value)

        return [names, valid_data[1]]

    def name_exists(self, name):
        for object in self._flyweight_list:
            if name == object.name:
                return object
        return False

    def printing(self):
        for object in self._flyweight_list:
            print(object.name)

    @property
    def flyweight_list(self):
        return self._flyweight_list


class Flyweight:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
