print("In this program, you will enter a lower and upper number to create a range, and then the program will list all the prime numbers within that range.")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")

lower = int(input("Please enter the lower number: "))
upper = int(input("Please enter the upper number: "))

print("The prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)