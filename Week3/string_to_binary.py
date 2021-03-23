"""
Complete the str_to_binary function.
"""
from helper_functions import binary, FIX_ME


def str_to_binary(input_string):
    for character in input_string:
        int1 = ord(character)
        bin1 = bin(int1)
        print(f'{bin1} ', end='')
    print('')



if __name__ == '__main__':
    str_to_binary('hello')  # Should print the line: 0b1101000 0b1100101 0b1101100 0b1101100 0b1101111
