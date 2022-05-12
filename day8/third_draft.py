alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

def encode_decode(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount*= -1
#what if a user enters any input that is not in the list of alphabets? he we do this
   
    for char in start_text:
        if char in alphabet:
          position = alphabet.index(char)
          new_position = position + shift_amount
          end_text+= alphabet[new_position] 
        else:
            end_text+=char

    print(f'your {direction}d result: {end_text}')




#****************************avoiding duplication*********************************

#what if we want the user to encode more than once?
keep_going = True
while keep_going:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

#what if a user enters a number greater than the alphabet?
    shift = shift%26
    encode_decode(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to continue, and 'no' if you do not want to continue\n")
    if result == 'no':
        keep_going = False
        print('goodbye')