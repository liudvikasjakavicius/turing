# First, we will get user input
response = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

# We need to print "Yes" if the user inputs "42," "forty-two," or "forty two" (case-insensitive)
if response.strip() == "42":
    print("Yes")
elif response.lower().strip() == "forty-two":
    print("Yes")
elif response.lower().strip() == "forty two":
    print("Yes")
# Output "No" for otherwise
else:
    print("No")