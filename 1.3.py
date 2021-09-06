def isBalanced(a):
    b = 0
    c = 0
    for i in range(0, len(a)):
        if (a[i] == '(' or a[i] == '{' or a[i] =='[' ):
            b += 1                               #if there’s an open parenthesis then b=b+1
        else:
            b -= 1                                #if there’s a closed parenthesis then b=b-1

        if (b == -1):
            c += 1
            b += 1
    if(b+c%2==0) :    #add the total number of open and closed parenthesis
        print("Yes")
    else:
        print("NO")
b=0
a = str(input("Enter the parenthesis: "))
for i in range(len(a)):
    if(a[i] == '(' or a[i] == '{' or a[i] =='[' or a[i] == ')' or a[i] == '}' or a[i] ==']' ):
        b=1
    else:
        print("Wrong input")
        break
if (b==1):
    print(isBalanced(a))



