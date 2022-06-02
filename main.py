print("Welcome To Lavya's Calculator")
x = input("""What Would U Like To Do?
Add
Subtract
Divide
Multiply\n\n""")

if x == "Add" or "add":
    num1 = input("Okay! What Would Be You're First Number?")
    num2= input("What's You're 2nd Number?")
    print("Okay! The Answer Is Below")
    print(int(num1) + int(num2))
    print("Thanks For Using Lavya's Calculator!")
    exit()

if x == "Subtract" or "subtract":
    num3 = input("Okay! What Would Be You're First Number?")
    num4 = input("What's You're 2nd Number?")
    print("Okay! The Answer Is Below")
    print(int(num3) - int(num4))
    print("Thanks For Using Lavya's Calculator!")
    exit()


if x == "Divide" or x == "divide":
    num5 = input("Okay! What Would Be You're First Number?")
    num6 = input("What's You're 2nd Number?")
    print("Okay! The Answer Is Below")
    print(int(num5) / int(num6))
    print("Thanks For Using Lavya's Calculator!")
    exit()


if x == "Multiply" or x == "multiply":
    num7 = input("Okay! What Would Be You're First Number?")
    num8 = input("What's You're 2nd Number?")
    print("Okay! The Answer Is Below")
    print(int(num7) * int(num8))
    print("Thanks For Using Lavya's Calculator!")
    exit()

