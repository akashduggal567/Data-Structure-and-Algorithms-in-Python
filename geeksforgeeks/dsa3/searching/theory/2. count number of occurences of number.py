arr = [1,2,2,3,3,3,3,20,40,50]

""" Sol-1 --> Linear search"""

def linearSearch(arr,size,num):     # time complexity --> O(n)
    count = 0
    for i in range(0,size):
        if arr[i] == num:
            count += 1
        elif arr[i] > num:          #optimization
            break
    if count == 0:
        return 0 
    return count

num = 2
print("count of",num,"is",linearSearch(arr,len(arr),num))

""" Sol-2 --> Binary Search """
"""
step 1 --> find first occurence of the element. let it be i
step 2 --> find last occurence of the element . let it be j
step 3 --> return (j-i+1)   ---> count/frequency

"""
def binarySearch(arr,size,num):

    first = findOccurence(arr,size,num,True)
   
    if first == -1 :
        return 0
    else:
        last = findOccurence(arr,size,num)
        return (last-first+1)

def findOccurence(arr,size,num,searchFirst = False):
    low = 0 
    high = size-1
    result = -1
    while low<=high:
        mid = (low+high)//2

        if num == arr[mid]:
            result = mid
            if(searchFirst):
                high = mid - 1
            else:
                low = mid + 1

        elif num> arr[mid]:
            low = mid +1
        else:
            high = mid -1
    return result

num = 3
print("count of",num,"is",binarySearch(arr,len(arr),num))