#get a list from the user
#print the last element in the list
#you can use any method you are comfortable with

l1= []
list_size = int(input("Enter the number of elements to be added in the list"))
for i in range(list_size):
    ele = input ("Enter element")
    l1.append (ele)

print("The last item is", l1[-1])
    
