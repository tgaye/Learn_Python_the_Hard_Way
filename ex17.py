# ex.17 More Files
from sys import argv
from os.path import exists

script, from_file, to_file = argv
in_file = open(from_file).read()
# indata = in_file.read()

print(f"Copying from {from_file} to {to_file}")
print(f"The input file is {len(in_file)} bytes long.")
print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

out_file = open(to_file, 'w').write(in_file)
# out_file.write(indata)
# print('Alright, all done.')

# out_file.close()
# in_file.close()

# study drills:
    # 1. Make script more friendly by removing features (commented out)

# mistakes made:
    # "You probably did something like this, indata =
    # open(from_file).read(), which means you don’t need to then do
    # in_file.close() when you reach the end of the script. It should already be
    # closed by Python once that one line runs."
