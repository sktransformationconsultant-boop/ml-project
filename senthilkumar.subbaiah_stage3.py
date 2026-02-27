def grade_calculator(name, mark1, mark2, mark3):
    # Calculate total marks
    total = mark1 + mark2 + mark3
    
    # Calculate percentage
    percentage = (total / 300) * 100
    
    # Determine grade
    if percentage >= 75:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 40:
        grade = 'C'
    else:
        grade = 'F'
    
    # Display results
    print(name)
    print(f"Total: {total}/300")
    print(f"Percentage: {percentage:.1f}%")
    print(f"Grade: {grade}")


# Example usage
grade_calculator("Raj", 80, 70, 90)
