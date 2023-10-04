# Get user input for an arithmetic expression
expression = input("Expression: ")
# Split the expression into x, y, and z
x, y, z = expression.split()
# Convert x and z to integers
x = int(x)
z = int(z)
# Initialize the result variable
result = None
# Perform the calculation based on the operator
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    if z != 0:
# Check for division by zero
        result = x / z
# Check if a valid result was calculated
if result is not None:
    # Print the result as a floating-point value formatted to one decimal place
    print(f"Result: {result:.1f}")