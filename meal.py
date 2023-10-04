# Define the main function
def main():
    # Get user input for the time
    time = input("Tell me the time: ").strip()
    # Call the convert function to convert the input to a floating-point number
    converted_time = convert(time)
    # Check if it's breakfast time (between 7:00 and 8:00)
    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")
    # Check if it's lunchtime (between 12:00 and 13:00)
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    # Check if it's dinner time (between 18:00 and 19:00)
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")
    # If none of the above conditions match, return without printing anything
    else:
        return
# Define a function to convert a time string to a floating-point number
def convert(time):
    # Split the time string into hours (x) and minutes (y)
    x, y = time.split(":")
    # Convert hours to a floating-point number
    hr = float(x)
    # Convert minutes to a fraction of an hour (floating-point number)
    mins = float(y) / 60
    # Calculate and return the total time as a floating-point number
    return hr + mins
# This block ensures that the main function is exected when the script is run
if __name__ == "__main__":
    main()