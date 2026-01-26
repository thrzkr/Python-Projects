num1 = int(input())
num2 = int(input())

if num1 >= num2:
    print("Invalid input")
    exit()
else:
    for number in range(num1, num2 + 1):
        double_number = number * 2
        print(f"{number} \t {double_number}")
