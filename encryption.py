alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TO do: encrypt function, decrypt function, caeser function

# encrypt function

def encrypt(original_text, shift_amount):
    ciphertext = ""
    for i in original_text:
        index = alphabet.index(i) + shift_amount
        ciphertext += alphabet[index]
    print(ciphertext)

# Decrypt function

def decrypt(original_text, shift_amount):
    ciphertext = ""
    for i in original_text:
        index = alphabet.index(i) - shift_amount
        ciphertext += alphabet[index]
    print(ciphertext)

# Caeser function that's taking in 3 arguments.  
def caeser(user_direction, texts, shifts):
    
    if user_direction == "encode":
        ciphertext = ""
        for i in texts:
            index = (alphabet.index(i) + shifts) % 26
            ciphertext += alphabet[index]
        print(ciphertext)
    else:
        ciphertext = ""
        for i in texts:
            index = (alphabet.index(i) - shifts) % 26
            ciphertext += alphabet[index]
        print(ciphertext)

    goagain = True

    while goagain:
        wants_to_go_again = input("Do you want to go again? Yes or No? ").lower()
        if wants_to_go_again == "yes":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            caeser(user_direction=direction, texts=text, shifts=shift)
        else:
            goagain = False
            print("Thank you for playing!")
            quit()


caeser(user_direction=direction, texts= text, shifts=shift)