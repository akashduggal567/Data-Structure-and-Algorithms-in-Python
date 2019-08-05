arr = [1,2,3,10,4]


#Brute force solution  (DISADVANTAGE --> Take extra space for temporary array)

arr_temp = []                               #declare an temporary array and append the element in reverse order to it
for i in reversed(range(len(arr))):
    arr_temp.append(arr[i])
print("reversed array = ", arr_temp)

#2-way pointer Technique

low = 0
high = len(arr)-1
while(low < high):
    arr[low], arr[high] = arr[high], arr[low] #swap low and high element
    low = low +1
    high = high -1
print("Using 2-way Pointer Technique = ", arr)

""" Time Complexity = O(n) and the above solution is an ITERATIVE SOLUTION"""

