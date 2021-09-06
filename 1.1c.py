#Part 1, Q.no. 1C
dict={
    "Sedan": 1500,
    "SUV": 2000,
    "Pickup": 2500,
    "Minivan": 1600,
    "Van": 2400,
    "Semi": 13600,
    "Bicycle": 7,
    "Motorcycle": 110
}
a=[key.upper() for key, value in dict.items() if value < 5000]
print(a)
