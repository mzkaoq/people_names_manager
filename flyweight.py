
from serviceInterface import ServiceInterface

class FlyweightFactory(ServiceInterface):
    def __init__(self):
       self._tree = Flyweight("root")


    def add_to_stack(self,valid_data):
        temporary_parent = self._tree
        for name in valid_data[0]:
            returned = self.looking_for_name(temporary_parent,name)
            if returned != None:
                temporary_parent = returned
            elif returned == None:
                new_child = Flyweight(name)
                print(id(new_child),name)
                temporary_parent.add_children(new_child)
                temporary_parent = new_child


    def looking_for_name(self,parent,name):
        children = parent.children
        for child in children:
            if child.name == name:
                return child
            else:
                pass
        return None

    def printing(self,root,tab):
        temp_parent = root
        children = temp_parent.children
        print(2*tab * " ","lvl",tab," ",temp_parent.name, id(temp_parent))
        new_tab = tab +1
        if len(children) > 0:
            for child in children:
                self.printing(child,new_tab)



    @property
    def tree(self):
        return self._tree

class Flyweight:
    def __init__(self,name):
        self._name = name
        self._children = []
        self.cords = []

    def add_children(self,child):
        self._children.append(child)

    def add_cord(self,cords):
        self.cords.append(cords)

    @property
    def name(self):
        return self._name

    @property
    def children(self):
        return self._children