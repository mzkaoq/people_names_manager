from flyweight import Flyweight

class Tree:
    def __init__(self):
       self._tree = Node(Flyweight("Node"))

    def add_to_stack(self,valid_data):
        temporary_parent = self._tree
        for name in valid_data[0]:
            returned = self.looking_for_name(temporary_parent,name)
            if returned != None:
                temporary_parent = returned
            elif returned == None:
                new_child = Node(name)
                temporary_parent.add_children(new_child)
                temporary_parent = new_child
        temporary_parent.add_cord(valid_data[1])

    def looking_for_name(self,parent,name):
        children = parent.children
        for child in children:
            if child.name.name == name.name:
                return child
            else:
                pass
        return None

    def printing(self,root,tab):
        temp_parent = root
        children = temp_parent.children
        cords = temp_parent.cords
        print(4*tab * " ","lvl",tab," ",temp_parent.name,temp_parent.name.name, id(temp_parent),cords)
        new_tab = tab +1
        if len(children) > 0:
            for child in children:
                self.printing(child,new_tab)


    @property
    def tree(self):
        return self._tree

    @tree.setter
    def tree(self,value):
        self._tree  = value

class Node:
    def __init__(self,name):
        self._name = name
        self._children = []
        self._cords = []

    def add_children(self,child):
        self._children.append(child)

    def add_cord(self,cords):
        self._cords.append(cords)

    @property
    def name(self):
        return self._name

    @property
    def cords(self):
        return self._cords

    @property
    def children(self):
        return self._children
