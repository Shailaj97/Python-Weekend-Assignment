#Part2 Q.no 6a
class range():
    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        x = self.i
        self.i +=1
        return x

range_obj = range()
my_iter = iter(range_obj)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#Part2 Q.no 6b
#Using generator

def range2(x):
    while x > 0:
        if x<5:
            yield x
        x -= 1

for i in range2(5):
    print(i)



