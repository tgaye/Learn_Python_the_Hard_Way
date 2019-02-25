# ex.14 Prompting and Passing
from sys import argv

script, user_name = argv
prompt ='> '

print(f"Hi, {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions")
print(f"Do you like me {username}?")
likes = input(prompt)

print(f'Where do you live {user_name}?')
lives = input(prompt)

print('What kind of computer do you have?')
computer = input(prompt)

print(f'''
Alright, so you said {likes} to liking me.
You live in {lives}, and have a {computer} computer.  Nice.
''')
