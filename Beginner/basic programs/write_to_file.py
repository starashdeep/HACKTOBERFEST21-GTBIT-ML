# we use "a" are because when we open a file we should not re-write we should just add it so that old records are not deleted
#if we use "w" the old records will be deleted 

f = open("myfile.txt","a")
L = ["Kesav \n", "PSG \n", "2025\n", "25" ]
f.writelines(L)
f.close()

"""
We can do like the above or we can insert one by one
f = open("myfile.txt","a")
f.write("Kesav\n")
f.write("PSG\n")
f.write("2025\n")
f.write("25\n")
f.close()
"""

"""
It is to get a input and then store it in a file
k = (input("Enter your name : "))
f = open("myfile.txt","a")
f.writelines(k)
f.close()
"""
