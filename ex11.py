# ex.11 User Inputs
print('How old are you?', end=' ')
age = input()

print('How tall are you?', end=' ')
height = input()

print('How much do you weigh (lbs?)?', end=' ') # imperial system bc im an ignorant American.
weight = input()

print(f'So, you\'re {age} old, {height} tall and {weight} lbs heavy'.format(age, height, weight)) #used esc key for fun

# mistakes: windows terminal with multiple input() prompts is a pain, use IDE
# study drill:
#   -3. Make your own form

print('What school did you go to?')
school = input()

print('What year did you graduate?')
year = int(input())

print(f'You graduated from {school} in the year {year}'.format(school, year))
