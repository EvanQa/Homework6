import random

num: int = random.randint(1, 100)
tries = 1
bet: int = int(input("enter a number"))
while bet > num:
    print("your number is too big")
    tries += 1
    bet: int = int(input("enter a number"))
    if bet < num:
        print("your number is too small")
        tries += 1
        bet: int = int(input("enter a number"))

else:
    print(f"BINGO you guess after {tries} tries")
