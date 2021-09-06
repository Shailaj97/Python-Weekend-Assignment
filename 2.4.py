#part 2 ,Q.no. 4
class ComplexNumber:
    def __init__(self, a):
        self.a = a

    def __add__(self, b):
        return self.a + b

    def __iadd__(self, b):
        self.a = self.a + b
        return self.a

    def __eq__(self, b):
        return self.a == b

    def __lt__(self, b):
        return self.a < b

    def __mul__(self, b):
        return self.a * b

    def __div__(self, b):
        return self.a / b

    def __floordiv__(self, b):
        return self.a // b

    def __pow__(self, b):
        return self.a ** b

    def __mod__(self, b):
        return self.a % b


c= ComplexNumber(2)
c.__add__(3)
c.__div__(2)

