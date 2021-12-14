
class DataInput():
    def __init__(self):
        pass

    def insert_data(self):
        names = []
        while True:
            print("insert name/surname or skip")
            data = input()
            if len(names) > 0 and data == "":
                break
            if data != "": names.append(data)
        print("insert cord X")
        cord_x = input()
        cord_x = self.number_input_corrector(cord_x)
        print("insert cord Y")
        cord_y = input()
        cord_y = self.number_input_corrector(cord_y)
        return [names, [cord_x, cord_y]]

    def number_input_corrector(self ,number):
        return float(number.replace(",", "."))
