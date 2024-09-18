num = 0
while True:
    num: int = int(input("Enter a number"))
    if num % 5 == 0 and num % 3 == 0:
        print("Fizz Buzz")
        break
    if num % 5 == 0:
        print("Fizz")
    if num % 3 == 0:
        print("Buzz ")
        break