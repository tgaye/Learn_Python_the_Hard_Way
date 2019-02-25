# ex.13 Parameters, Unpacking, Variables
from sys import argv # argument variable, holds arguments passed to script

# read the WYSS section for how to run this
script, first, second, third = argv # unpack argv
print('The script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is:', third)

#study drills:
#   -3. Combine input with argv to make a script that gets more input from a user.
choice = input('Which variable would you like to see?')
if choice.lower() == 'first' or choice == '1st' or choice == '1':
    print(first)
if choice.lower() == 'second' or choice == '2nd' or choice == '2':
    print(second)
if choice.lower() == 'third' or choice == '3rd' or choice == '3':
    print(third)
else:
    print('invalid input: (first|second|third)')
