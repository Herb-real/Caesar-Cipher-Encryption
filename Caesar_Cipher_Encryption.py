#Group 3
#Caeser Encryption

# List of characters of the alphabets
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z']


# Define function to encrypt  text
def caesar(start_text, shift_amount):
    # Initialize that resulting text variable
    end_text = ""

    # encoding text => negate the shift direction
    shift_amount *= -1

    for char in start_text:
        # Encrypt 
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        # Preserve spaces and symbols the text/cypher text
        else:
            end_text += char
    # Print the encoded text
    print(f"Encrypted message: {end_text}")


# Keep game going for as long as user wishes
should_end = False
while not should_end:
    text = input("Type your plain message:\n").upper()
    shift = int(input("Type the shift number:\n"))

    # Prevent shift errors
    shift = shift % 26

    # Call function to encrypt or decrypt text
    caesar(start_text=text, shift_amount=shift)

    # Prompt user for next line of action
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Exiting...")
        
        