#take user input for the list
lst = []
n = int(input("enter number of elements:"))
for i in range(0, n):
    element = input()
    lst.append(element)
print(lst)

#take user input for which element are they looking for 
x = input("Enter element you were looking for:")

#iterate through the list and report the number of times the particular element  occured in the list
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

print("There are {} occurrences".format(countX(lst,x)))
