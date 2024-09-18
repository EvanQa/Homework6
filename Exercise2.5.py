sum_temps: int = 0
for _ in range(5):
    temp = int(input('enter a temperature of your city '))
    if temp < -51 or temp >= 45:
        print("wrong temperature")
        temp = int(input('enter a temperature of your city '))
    sum_temps += temp
else:
    avg = sum_temps / 5
    print(f"average of temperature = {avg: .0f}")