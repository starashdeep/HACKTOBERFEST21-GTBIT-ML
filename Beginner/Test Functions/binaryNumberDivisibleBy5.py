n = input("Enter The binary number\n")
rev_n = n[::-1]

n_base4 = []

for i in range(0, len(n), 2):
    if i == len(n)-1:
        n_base4.append(int(rev_n[i]))
    else:
        n_base4.append(int(rev_n[i]) + 2*int(rev_n[i+1]))

odd_sum = 0
even_sum = 0

for i in range(0, len(n_base4)):
    if i % 2 == 0:
        even_sum += n_base4[i]
    else:
        odd_sum += n_base4[i]

if(abs(odd_sum-even_sum) % 11 == 0):
    print("Input binary number is divisible by 5")
else:
    print("Input binary number is not divisible by 5")
