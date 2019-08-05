""" To find leaders in an array . Meaning -> no element should be there in the right of the leader greater than the leader """

""" Disadvantage --> O(N^2)"""
def bf(arr,size):
    for i in range(0,n):
        for j in range(i+1, n):
            if arr[j] >= arr[i]:
                break
        if j == n-1:
            print(arr[i])
                
""" O(N) solution"""
import collections

def leader(arr,size):
    max = arr[size-1]
    s = collections.deque()
    s.append(max)
    for i in reversed(range(0,size-1)):
        if max < arr[i]:
            s.append(arr[i])
            max = arr[i]
    while(s):
        print(s.pop())
        


arr = [5, 3, 20, 15, 8, 3]
n = len(arr)
print("BF Technique, Leaders in the array = ")
bf(arr,n)
print("Optimized technique")
leader(arr,n)