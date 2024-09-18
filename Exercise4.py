
count = 0
num = 7
while num % 7 == 0:
    num = int(input(" enter a number: "))
    count += 1
    if num % 11 == 0:
        break
else:
    print(f"count is: {count}")




