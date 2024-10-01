'''
Name: Mr. Smith
Date: 10/1/24
Description: Salad ingredient amount generator
'''

# Step 1: Get the names of the ingredients and their ounces
ingredient_one = input("Enter ingredient 1: ")
ounces_of_one = float(input(f"Ounces of {ingredient_one}: "))
ingredient_two = input("Enter ingredient 2: ")
ounces_of_two = float(input(f"Ounces of {ingredient_two}: "))
ingredient_three = input("Enter ingredient 3: ")
ounces_of_three = float(input(f"Ounces of {ingredient_three}: "))

# Step 2: Get the number of servings
num_servings = int(input("Enter number of servings: "))

# Step 3: Calculate the total ounces for each ingredient
total_ingredient_one = ounces_of_one*num_servings
total_ingredient_two = ounces_of_two*num_servings
total_ingredient_three = ounces_of_three*num_servings

# Step 4: Print the total ounces for each ingredient
print(f"Total ounces of {ingredient_one}: {total_ingredient_one:.2f}")
print(f"Total ounces of {ingredient_two}: {total_ingredient_two:.2f}")
print(f"Total ounces of {ingredient_three}: {total_ingredient_three:.2f}")
