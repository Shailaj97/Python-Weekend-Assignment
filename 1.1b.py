#Part 1 , Q.no 1B
def myfunc(a):
    frequency = {}

    for i in a:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    print("The count of the giver characters is : " +str( frequency))

result  = myfunc ("aaaaabbbbcccdde")
print(result)