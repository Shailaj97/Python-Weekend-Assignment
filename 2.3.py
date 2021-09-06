#Part 2, Q.no 3
class phone:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    @property
    def radio(self):
        print(self.radio)

    @radio.setter
    def radio(self, fm):
        self.radio = dm

    @staticmethod
    def expensive(price):
        return price > 10000



    @classmethod
    def usingString(cls, string):
        brand, color, price = string.split(',')
        return cls(brand, color, int(price))

