"""
Complete the lines that have TODO: comments above them.
"""

from helper_functions import FIX_ME
from string_with_spaces import str_to_spaces
from string_to_ascii_codes import str_to_ascii_codes
from string_to_hex import str_to_hex
from string_to_binary import str_to_binary
from xor import xor


def one_time_pad(plaintext, key):
    # 1. Check if the key is long enough. Raise an exception with an error message if it's not
    if len(key) < len(plaintext):
        raise Exception('Key is too short. Aborting')

    # 2. Print each of the plaintext characters in ASCII separated by spaces. Use print_as_chars() above for help. e.g. If plaintext is 'hello' then print 'h e l l o'
    print('Plaintext:')
    str_to_spaces(plaintext)

    # 3. Print the integer value for each character separated by spaces. e.g. If plaintext is 'hello' then print 104 101 108 108 111
    print('Plaintext ASCII Codes:')
    str_to_ascii_codes(plaintext)

    # 4. Print the hex representation for each character. e.g. If plaintext is 'hello' then print 0x68 0x65 0x6c 0x6c 0x6f
    print('Plaintext Hex:')
    str_to_hex(plaintext)

    # 5. Print the binary representation of each character. e.g. If plaintext is 'hello' then print 0b01101000 0b01100101 0b01101100 0b01101100 0b01101111
    print('Plaintext Binary:')
    str_to_binary(plaintext)

    # 6. Do steps 2-5 again for the key.
    print('Key:')
    str_to_spaces(key)

    print('Key ASCII Codes:')
    str_to_ascii_codes(key)

    print('Key Hex:')
    str_to_hex(key)

    print('Key Binary:')
    str_to_binary(key)

    print('Performing XOR')
    # 7. Perform an XOR on each plaintext character and key then save the result.
    temporary_list = []

    for i in range(len(plaintext)):
        # Don't change these 2 lines.
        plaintext_ascii_code = ord(plaintext[i])
        key_ascii_code = ord(key[i])

        # TODO: Perform an XOR.
        ciphertext_ascii_code = xor(plaintext_ascii_code, key_ascii_code)

        # TODO: Convert the ciphertext ascii code back to a character.
        ciphertext_character = chr(ciphertext_ascii_code)  # TODO: Convert ciphertext_ascii_code back to a character.
        
        # TODO: Add the character to your temporary list
        temporary_list.append(ciphertext_character)

    # Print the contents of your temporary list
    print(f'Temporary List: {temporary_list}')

    # Join the list characters together using Python's string join function: ''.join(some_list)
    ciphertext = ''.join(temporary_list)

    # 8. Repeat steps 2-5 for the result.
    print('Ciphertext Binary:')
    str_to_binary(ciphertext)

    print('Ciphertext Hex:')
    str_to_hex(ciphertext)

    print('Ciphertext ASCII Codes:')
    str_to_ascii_codes(ciphertext)

    print('Ciphertext:')
    str_to_spaces(ciphertext)



if __name__ == '__main__':
    # Call/run the function and check the output
    one_time_pad('Lavinia Tuitahi','theonetimepadismucheasierwithcomputers')

