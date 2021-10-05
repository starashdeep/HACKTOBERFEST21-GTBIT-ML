import random

num=int(input("Enter length of password :: "))
if num>4:
    dig,low_alpha,upper_alpha,spcl_chr=[],[],[],[]
    for i in range(10):
        dig.append(str(i))

    for i in range(26):
        low_alpha.append(chr(65+i))
        upper_alpha.append(chr(97+i))
    for i in range(7):
        spcl_chr.append(chr(58+i))

    combined_ls=dig+upper_alpha+low_alpha+spcl_chr

    compusory=[random.choice(dig),random.choice(spcl_chr),random.choice(low_alpha),random.choice(upper_alpha)]

    for i in range(num - len(compusory)):
        compusory.append(random.choice(combined_ls))
    random.shuffle(compusory)
    password=""
    password=''.join(compusory)
    print ("Password Randomly Generated :: " + password)

else :
    print("Wrong Input")
