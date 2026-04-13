
# Prime number checker in Python

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Prime check logic
if num < 2:
    print(f"{num} is not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")