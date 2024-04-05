def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed"
    else:
        return "Error: Invalid operator"

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an arithmetic operation (+, -, *, /): ")
    
    result = calculate(num1, num2, operator)
    print("The result is: ", result)

if __name__ == "__main__":
    main()