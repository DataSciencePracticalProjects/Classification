"""
Create a function that takes a list of integers and returns what the
smallest number is in.
Do not use built-in functions.
eg for the list [42, 13, 56, 7, 12, 3, 85] the function should return 5, because
the smallest element is found at this index in this list.
"""

def smollest(list_in):
    res = int(list_in[0])
    for num in list_in:
        if int(num) < res:
            res = int(num)
    return res


if __name__ == '__main__':
    list_int = [5, 4, 25, 100, 8, 9, 47, 1, -100]
    print(list_int.index(smollest(list_int)))