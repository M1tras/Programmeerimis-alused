# Write your code here
first_name = "James"
last_name = "Bond"

full_name = first_name + " " + last_name
self_description_sentence = "My name is " + last_name +", " + full_name + "."


cake = "vahukoormarjadtäidispõhi"
cake_ingredient_1 = cake[0: 8]
cake_ingredient_2 = cake[8: -10]
cake_ingredient_3 = cake[14: -4]
cake_ingredient_4 = cake[20: 24]
cake_ingredients = [cake_ingredient_1, cake_ingredient_2, cake_ingredient_3, cake_ingredient_4]
for ingredient in cake_ingredients:
    print(ingredient)
    

original_string = "Programming is fun!"
backwards = original_string[::-1]

original_string = "Programming is fun!"
every_other = original_string[0:19:2]

first_word_reversed_beta = original_string[0: 11]
first_word_reversed = first_word_reversed_beta[::-1]
