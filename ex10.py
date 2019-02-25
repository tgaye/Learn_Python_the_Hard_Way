# ex.10 Intro to Escape Sequences
print("I am 6'2\" tall.") # escape double quote
print('I am 6\'2" tall.') # escape single quote

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"# esc char with new line
backslash_cat = "I'm \\ a \\ cat."# esc char with backslash

# list with each item tabbed
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# mistakes: / instead of \
# study drills:
#   -3. Combine escape sequences and format strings to create a more complex

print('I am {} tall.'.format('6\'2"'))
