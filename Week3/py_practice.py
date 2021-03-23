#-------------------Conversion------------------------------------------

# converts string to integer
x = int('240')
a = type(x)
print(a)

#converts a hexadecimal string into an integer
x = int('0xFE', base=16)
print(x)

#int() will only accept a number. Passing another data type through will cause an error
try:
    int('hello')
except ValueError:
    print('Caught and ignoring an exception when trying int("hello")')

#converts integer into hex string
a = hex(195)
print(a)

#hex() only accepts integers and not strings. A string will cause an error
try:
    hex('195')
except TypeError:
    print('Caught and ignoring an exception when trying hex("195")')

#converts integer to binary
a = bin(205)
print(a)

## By default Python doesn't display leading-zeros when printing a binary number.
print(bin(13))  # Will only display '0b1101'

# use binary() function in helper_functions to fix above issue

from helper_functions import binary
print((binary(13)))

#bin() only accepts integers and not strings. Exception thrown
try:
    bin('123')
except TypeError:
    print("Caught and ignoring an exception when trying bin('123')")

#Looks up ASCII code for a single character string and returns corresponding integer
print((ord('X')))

#ord() only accepts a single character
try:
    ord('hello')
except TypeError:
    print("Caught and ignoring an exception when trying to run ord('hello')")

#converts integer into ASCII code character
print((chr(72)))

#chr() only accepts integers
try:
    chr('f')
except TypeError:
    print('Caught and ignoring an exception when trying to run chr("f")')


#--------------------------Strings with Spaces---------------------------------------------

#Takes a string and prints it with spaces in between each character. Breaks a string into individual characters and prints them one at a time.

def str_to_spaces(input_string):
    for character in input_string:
        print(f'{character} ', end='') # The extra space is needed. end='' stops print() from making a new line for each character.
    
    print('') # Print an empty line after the loop. What happens if we delete this part? What happens if we remove , end='' above?

    if __name__=='_main_':
        str_to_spaces('hello') # displays the string 'hello'

# Example of use of str_to_spaces function
x = input('What is your name? ')
print(str_to_spaces(x))

#-----------Helper functions---------------
# Must use from and import keywords to import function into current file so it can be used

