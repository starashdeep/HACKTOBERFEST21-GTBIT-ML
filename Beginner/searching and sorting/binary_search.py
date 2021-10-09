def binary_search(data, key):

    low = 0
    high = len(data) - 1

    while low <= high:
      
        middle = (low + high)//2
       
        if data[middle] == key:
            return middle
        elif data[middle] > key:
            high = middle - 1
        else:
            low = middle + 1

    return -1
    
data = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 

for i in range(0, n):
    x = int(input())
 
    data.append(x)
     
print(data)
print("sorted array is ",sorted(data))
key = int(input("Enter Key : "))
print("Key found at ",binary_search(sorted(data), key)," index")
