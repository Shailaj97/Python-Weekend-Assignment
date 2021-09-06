#Par2, Q.no.2a
#Custom Error implemented using class

class AgeGroup(Exception):
    #Exception raised for errors if the age is not in range


    def __init__(self, age, message="Your age is not in the (18, 60) age group"):
        self.age= age
        self.message = message
        super().__init__(self.message)


age = int(input("Enter your age: "))
if not 18 < age < 60:
    raise AgeGroup(age)
else:
    print("You are getting old")