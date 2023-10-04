def main():
# Prompt the user to enter a license plate
    plate = input("Plate: ")
# Check if the entered license plate is valid and print the result
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
# Check if the length of the input is between 2 and 6 characters and contains only alphanumeric characters
    if 2 <= len(s) <= 6 and s.isalnum():
# "Return `True` if all the characters are alphabetic.
        if s.isalpha():
            return True
        else:
# Check for a number in the middle of the input
            if s[:2].isalpha() and s[-2:].isdigit():
                for i in range(len(s)):
# If a digit is encountered
                    if s[i].isdigit():
# Return `False` if a number begins with 0 or if the next character is a letter
                        if s[i].startswith("0") or s[i:].isalpha():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False
#End of program
main()