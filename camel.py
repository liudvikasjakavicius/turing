# Get user input
camelCase = input("camelCase: ")
# Print the snake_case variable name
print("snake_case: ", end="")
# Loop through each character in the camelCase name
for character in camelCase:
    if character.islower():
# Check if the character is lowercase
        print(character, end="")
# If lowercase, print it as is
    if character.isupper():
# Check if the character is uppercase
        print("_", character.lower(), end="", sep="")  # If uppercase, print an underscore followed by the lowercase character
# Print
print()