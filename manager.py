from data_input import DataInput
from proxy import Proxy
from tree_maker import Tree
import json
from json import JSONEncoder

class Manager:
    def __init__(self):
        self._data_input = DataInput()
        self._proxy = Proxy()
        self._tree = Tree()
        self.manager()

    def manager(self):
        while True:
            print("enter \n1 to add new person\n2 show all persons\n3 to save in JSON\n4 to load from JSON\n5 to close")
            option = int(input())
            if option == 1:
                """
                data = self._data_input.insert_data()
                print(data)
                x = self._proxy.add_to_stack(data)
                self._tree.add_to_stack(x)
                """
                x = self._proxy.add_to_stack([["MiChal","adAm","MAciEk","pATrYk"],[23,12]])
                self._tree.add_to_stack(x)
                x = self._proxy.add_to_stack([["MIchal","WOjTek","maCIek","krystian"],[82,55]])
                self._tree.add_to_stack(x)
                x = self._proxy.add_to_stack([["kACpEr","ADAM","lUkAsZ","damian"],[19,30]])
                self._tree.add_to_stack(x)
                x = self._proxy.add_to_stack([["MiKOLaj","pioTR","ADaM","kRySTiaN"],[3,42]])
                self._tree.add_to_stack(x)
                x = self._proxy.add_to_stack([["miChAL","ZbIGNiEW","maCiEK"],[16,19]])
                self._tree.add_to_stack(x)
                x = self._proxy.add_to_stack([["KaCPer","ZBiGNIew","luKAsZ","PATRyK","SebASTIiAn"],[2,1]])
                self._tree.add_to_stack(x)

            elif option == 2:
                self._tree.printing(self._tree.tree,1)
            elif option == 3:
                tree2 = json.dumps(self._tree.tree, indent=10,cls=Encode)
                with open('data.json', 'w') as f:
                    json.dump(tree2, f)
            elif option == 4:
                with open('data.json') as json_file:
                    data = json.load(json_file)
                print(type(data))
                self._tree = Tree()
                self._tree.tree = json.loads(data)
                print(self._tree.tree)
            elif option == 5:
                break

class Encode(JSONEncoder):
    def default(self, o):
        return o.__dict__