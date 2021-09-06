#Part2, Q.no.2b
#Custom Error using Exception or BaseException class using message to handle at least two of the cases.

class Error(Exception):
    #Base class
    pass

class LargeValueError(Error):
    pass

class SmallValueError(Error):
    pass

number = 10

while True:
    try:
        a = int(input("Guess the right number: "))
        if a < number:
            raise ValueTooSmallError
        elif a > number:
            raise ValueTooLargeError
        break
    except SmallValueError:
        print("This value is too small ")
        print()
    except LargeValueError:
        print("This value is too large ")
        print()

print("You've guessed the right number")