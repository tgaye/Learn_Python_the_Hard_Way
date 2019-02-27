# ex.19 Functions and variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("Or we can use variables from out script.")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print('We can even do math inside too:')
cheese_and_crackers(10+20, 5+6)

print('And we can combine the two, variables and math:')
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 20)

# study drill:
    # write a function of your own, run multiple ways.
def weight_conversion(lbs):
    kg = lbs * .453592
    return kg

weight = 200
kg = weight_conversion(weight) # function with variable
print(kg)
kg = weight_conversion(150) # function with value passed through
print(kg)
kg = weight_conversion(int(input('Input your weight in lbs.'))) # function w user input
print(kg)

# tips: function variables are temporary, return their values if you want to work with them.
