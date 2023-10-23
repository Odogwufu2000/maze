def convert_number(phone_number):
    # Define a dictionary to map alphabetic characters to their numeric equivalent
    letter_to_digit = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }

    # Initialize an empty result string
    result = ""

    # Iterate through each character in the input phone number
    for char in phone_number:
        # Check if the character is alphabetic
        if char.isalpha():
            # Convert the alphabetic character to its numeric equivalent
            result += letter_to_digit.get(char.upper(), char)
        else:
            result += char

    return result

# Example usage:
input_phone_number = input(str("Enter a telephone number: "))
converted_number = convert_number(input_phone_number)
print(" ",input_phone_number)
print(" ",converted_number)  # Output: "555-438-3663"
