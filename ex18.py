# ex.18 Names, Variables, Code, Functions

# this one is like your scripts with argv:
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do:
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this takes just one argument:
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments:
def print_none():
    print("I got nothin")

print_two('Tyler', 'Gaye')
print_two_again('Tyler', 'Gaye')
print_one('First!')
print_none()
