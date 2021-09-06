#Part 2, Q.no. 5
class List():
    def Cloning(list1):
        list2 = []
        list2.extend(list1)
        return list2

    # Driver Code
    list1 = [1,2,3,4,5]
    list2 = Cloning(list1)
    print("Original List:", list1)
    print("Clonned List:", list2)