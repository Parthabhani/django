response = input("Do you want to add two numbers? (yes/no): ")

if response.lower() == "yes" :
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = num1 + num2

    print("The result is: ", result)
else:
    print("Okay, no addition will be performed")