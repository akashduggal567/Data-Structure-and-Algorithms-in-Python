"""Given a SORTED ARRAY , find the index of the element if present"""

def binarySearch(arr,low,high,num):                 #recursive soln

    if low<=high:
        mid = (low + high)//2
        if arr[mid] == num:
            return mid
        elif num < arr[mid]:
            return binarySearch(arr,low,mid-1,num)
        else:
            return binarySearch(arr,mid+1,high,num)
    else:
        return -1

arr = [1,3,5,10,15,20,30]
print(binarySearch(arr,0,len(arr)-1,30))


def binarySearchIterative(arr,low,high,num):        # iterative solution
    while(low<=high):

        mid = (low+high)//2

        if num == arr[mid]:
            return mid
        elif num > arr[mid]:
            low = mid + 1
        else:
            high = mid-1
    return -1

print(binarySearchIterative(arr,0,len(arr)-1,30))