print("What do you want to do?")
print("1: Add ")
print("2: Subtract ")
print("3: Multiply ")
print("4: Divide ")

choice = input("Type 1, 2, 3, or 4: ")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
print("Calculating.")

if choice == '1':
    answer = num1 + num2
    print(f"The answer is: {answer}")
elif choice == '2':
    answer = num1 - num2                                                                                
    print(f"The answer is: {answer}")
elif choice == '3':
    answer = num1 * num2
    print(f"The answer is: {answer}")
elif choice == '4':
    if num2 == 0:
        print("You can't divide by zero !!")
    else:
        answer = num1 / num2
        print(f"The answer is: {answer}")
else:
    print("Invaild, try with a different number. :)")
