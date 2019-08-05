"""
Brute-force Solution                                            time complexity = O(n)  space-complexity = O(d)
        Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
        1) Store d elements in a temp array
        temp[] = [1, 2]
        2) Shift rest of the arr[]
        arr[] = [3, 4, 5, 6, 7, 6, 7]
        3) Store back the d elements
        arr[] = [3, 4, 5, 6, 7, 1, 2]
"""

                """To Rotate an array by d elements in anticlockwise direction"""
def reverse(arr,low,high):
    while(low<high):
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1

def rotate_anti(arr,d,n):
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
    return arr

arr = [5,8,10,12,15]
d = 2
n = len(arr)
print("Rotated Array = ",rotate_anti(arr,2,n))
