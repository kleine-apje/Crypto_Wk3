"""
Create a function named xor which takes two ascii codes,
prints their binary, then performs a bitwise XOR using the ^ (caret) operator,
prints the result of the XOR, then returns the result.
"""
from helper_functions import binary, FIX_ME

"""
Using code from the bitwise_and() function (see helper_functions.py), create an additional function called xor() which perform the XOR operation.
"""
def xor(integer_a, integer_b):
    print(f'The bitwise XOR of {binary(integer_a)} and {binary(integer_b)} is: ')
    result = (integer_a ^ integer_b)
    print(f'Result: {binary(result)}')
    return result



if __name__ == '__main__':
    xor(85, 170)

