



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

    return f"Result = {result}"


# Example usage
print(calculator(10, 5, '+'))  # Output: Result = 15
print(calculator(10, 0, '/'))  # Output: Error: Division by zero is not allowed.

