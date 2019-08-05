"""
x^x = 0
x^0 = x
"""
def find_odd_occuring_element(arr,size):
    num = 0
    for i in range(0,size):
        num = num^arr[i]
    print(num)

arr = [3,3,3,4,5,4,5]
find_odd_occuring_element(arr,len(arr))

""" time complexity --> O(n) """