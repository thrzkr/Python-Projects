print("1- Calories diet")
print("2- Low carb diet")
print("3- Keto diet")
s = int(input())
c = float(input())


def diet(x, y, z):
    carb = c*x
    fats = c*y
    prot = c*z
    print("Macros Details:")
    print("Calories from carbohydrates:", carb)
    print("Calories from fats:", fats)
    print("Calories from protein:", prot)

    if c < 1000:
        print("Invalid calories value")
    else:
        if s == 1:
            diet(0.5, 0.2, 0.3)
        elif s == 2:
            diet(0.15, 0.6, 0.25)
        elif s == 3:
            diet(0.05, 0.7, 0.25)
        else:
            print("Invalid selection")
