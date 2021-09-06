array_list = [1, 2, 3, 4, 5];

def rotateLeft(array):
    num_rotate=int(input("Enter the number of rotations you want: "));

    print("Original array: ");
    for i in range(0, len(array_list)):
        print(array_list[i]),


    for i in range(0, num_rotate):
        first = array_list[0];
        for j in range(0, len(array_list) - 1):
            array_list[j] = array_list[j + 1];

        array_list[len(array_list) - 1] = first;

    print();

    print("Array after left rotation: ");
    for i in range(0, len(array_list)):
        print(array_list[i]),

result=rotateLeft(array_list)
print(result)