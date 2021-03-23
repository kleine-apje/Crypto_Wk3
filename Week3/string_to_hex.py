"""
Create a function which takes a string and prints each character as decimal values corresponding to their ASCII codes.

Hint: Use string_with_spaces.py for help.
"""
from helper_functions import FIX_ME


def str_to_hex(input_string):
    for character in input_string:
        ascii_code = ord(character)  
        result = (hex(ascii_code))
        # Print the result
        print(f'{result} ', end='')
    print('')



if __name__ == '__main__':
    str_to_hex(input('Write your hex: '))  # This should print the line '0x68 0x65 0x6c 0x6c 0x6f'

