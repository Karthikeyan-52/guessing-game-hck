import random
print("Welcome to guessing game")
n1 = random.randint(1, 100)
while True:
    n2=int(input("Guess the number:"))
    if n1>n2:
        print("Your guess is too low")
    elif n1<n2:
        print("Your guess is too high")
    elif  n1==n2:
        print("Your guess is correct")
        break