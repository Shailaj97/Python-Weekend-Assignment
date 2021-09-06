#Part 2 Q.no. 1
#Create generator with and without comprehension for getting multiples of given number upto 10.
#Eg. generator(5) =>> 5, 10, 15 …. 50


#without comprehension
a=int(input("Enter a number: "))
for i in range(1,11):
    b=a*i
    print(b)

#With comprehension
a=int(input("Enter a number:"))
length=10
b=range(a,a*length+1,a)
print(*b)