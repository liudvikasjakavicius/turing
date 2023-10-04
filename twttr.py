def main():
    # Get input from the user
    text = input("Input: ")
    # Call the shorten function and print the result
    shortened_text = shorten(text)
    print("Output:", shortened_text)
def shorten(word):
    # Define a string of vowels (both lowercase and uppercase)
    vowels = "AEIOUaeiou"
    # Use a list comprehension to create a new string with non-vowel characters
    out = ''.join([char for char in word if char not in vowels])
    # Return the modified string with vowels removed
    return out
if __name__ == "__main__":
    # Call the main function when the script is run
    main()
