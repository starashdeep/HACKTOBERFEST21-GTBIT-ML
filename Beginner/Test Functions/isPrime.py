from math import sqrt

n = int(input("Enter the number\n"))

prime_flag = 0
 
if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        print("Input number is prime")
    else:
        print("Input number is not prime")
else:
    print("false")