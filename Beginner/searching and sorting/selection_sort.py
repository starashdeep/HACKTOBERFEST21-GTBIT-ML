import sys
A = []
n = int(input("Enter the number of elements : "))

# Taking input from the user 
for i in range(0, n):
    ele = int(input()) 
    A.append(ele)

for i in range(len(A)):

	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j
			
	
	A[i], A[min_idx] = A[min_idx], A[i]


print ("\nSorted array : ")
for i in range(len(A)):
	print("%d" %A[i]),
