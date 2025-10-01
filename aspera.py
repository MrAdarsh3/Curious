from num2words import num2words

def number_to_word():
    """Takes a numbef from the user & prints its word form."""
    try:
        user_input = int(input("Enter a number: "))
        word_form = num2words(user_input)
        print(f"Word Form: {word_form.title()}.")
    except ValueError:
        print("INVALID, Please enter a valid number!")

while True:
    number_to_word()
