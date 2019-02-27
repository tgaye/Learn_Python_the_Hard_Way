# ex.16 Reading and Writing Files
# .txt editor
from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to a file.")
target.write(line1 + "\n" + line2 + "\n" + line3) # drill 3
# target.write("\n") # unnecessary writes
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()

# drill 2
target_read = open(filename, 'r')
print(f"Here's your file {filename}:")
print(target_read.read())

# mistakes made:
    # cant read if opened explicitely with 'w' write, made new dummy var.

# study drills:
    # 2. Write a script similar to the last exercise that uses read and argv to read the file you just created.
    # 3. There’s too much repetition in this file. Rewrite with just one target.write() command instead of 6.

# helpful:
    # just doing open(filename) opens it in 'r' (read) mode by default.
