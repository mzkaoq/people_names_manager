from data_input import DataInput
from proxy import Proxy


class Manager:
    def __init__(self):
        self._data_input = DataInput()
        self._proxy = Proxy()
        self.manager()

    def manager(self):
        while True:
            print("enter \n1 to add new person\n2 show all persons\n3 to exit")
            option = int(input())
            if option == 1:
                data = self._data_input.insert_data()
                print(data)
                self._proxy.add_to_stack(data)
            elif option == 2:
                self._proxy.printing()
            elif option == 3:
                break
