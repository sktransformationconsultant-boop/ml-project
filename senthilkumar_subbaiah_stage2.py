def calculator(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            result = num1 / num2
    else:
        return "Error: Invalid operator."

    # Show result
    print(f"Result = {result}")

    # Check if result is positive, negative, or zero
    if result > 0:
        print("Positive")
    elif result < 0:
        print("Negative")
    else:
        print("Zero")


# Example usage
calculator(10, 5, '-')   # Output: Result = 5, Positive
calculator(5, 10, '-')   # Output: Result = -5, Negative
calculator(5, 5, '-')    # Output: Result = 0, Zero
calculator(10, 0, '/')   # Output: Error: Division by zero is not allowed.
