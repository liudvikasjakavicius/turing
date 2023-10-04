#initiating the program
def main():
# Get user input and make sure it can be in lower cases (.lower) and that spaces does not affect (.strip)
    greeting = input("Please enter a greeting: ").strip().lower()
#Check if the greeting has "hello" and print 0 USD.
    if greeting.startswith("hello"):
        print("$0")
#Check if the greeting has "h" and print 0 USD.
    elif greeting.startswith("h"):
        print("$20")
#If the greeting does not have "hello" or "h" then print 100 USD
    else:
        print("$100")

if __name__ == "__main__":
    main()