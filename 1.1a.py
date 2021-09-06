lst1=[100, 200, 300, 400, 500]
lst2=[1,10,100,1000,10000]
result=map(lambda x,y: x + y, lst1, lst2)
print("Adding the two lists we get:")
print(list(result))