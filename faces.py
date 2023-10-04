def convert(input_str: str):
    # Here we want to replace :) with 🙂 and :( with 🙁
    input_str = input_str.replace(':)', '🙂')
    input_str = input_str.replace(':(', '🙁')
    return input_str
def main():
    #Instructions for the user.
    print("Please enter any text with emoticons to convert them to emojis:")
    user_input = input()
    converted_text = convert(user_input)
    print("Converted text:")
    print(converted_text)
if __name__ == "__main__":
    main()