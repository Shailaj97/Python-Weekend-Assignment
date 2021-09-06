#Part 2, Q.no. 2c
def division(a, b):
    try:
              result = a / b
    except ZeroDivisionError:
        print("Zero division error has occured")
    else:
        print("Your answer is :", result)
    finally:
        print('Have a great day')


division(5, 2)
division(7, 0)