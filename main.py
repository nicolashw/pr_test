def main():
    with open("calculations.log", "w") as log_file:
        while True:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /) or 'q' to quit: ")
            if operation.lower() == 'q':
                break
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero is not allowed.")
                    log_file.write(f"Error: Division by zero is not allowed. Input: {num1}, {num2}, {operation}\n")
                    continue
            else:
                print("Error: Invalid operation.")
                log_file.write(f"Error: Invalid operation. Input: {num1}, {num2}, {operation}\n")
                continue
            print("Result:", result)
            log_file.write(f"Input: {num1}, {num2}, {operation}. Result: {result}\n")
if __name__ == "__main__":
    main()
