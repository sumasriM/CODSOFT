def calculate(expression):
    if "+" in expression:
        return add(expression)
    elif "-" in expression:
        return sub(expression)
    elif "*" in expression:
        return mul(expression)
    elif "/" in expression:
        return div(expression)
    elif "%" in expression:
        return re(expression)
    else:
        return "Invalid expression"
def add(expression):
    a, b = map(int, expression.split("+"))
    return a + b
def sub(expression):
    a, b = map(int, expression.split("-"))
    return a - b
def mul(expression):
    a, b = map(int, expression.split("*"))
    return a * b
def div(expression):
    a, b = map(int, expression.split("/"))
    if b != 0:
        return a / b
    else:
        return "Division by zero error"
def re(expression):
    a, b = map(int, expression.split("%"))
    return a % b
def main():
    print("Welcome to the calculator!")
    print("Operations supported: +, -, *, /, %")
    while True:
        command = input("Enter expression (or 'exit' to quit): ")
        if command.lower() == "exit":
            print("Exiting the calculator.")
            break
        result = calculate(command)
        print(f"Result: {result}")
main()