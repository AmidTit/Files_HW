import os
FILE_NAME = 'recipes.txt'
FILE_DIR = '2.4.files'
ROOT_PATH = os.getcwd()

full_path = os.path.join(ROOT_PATH, FILE_DIR, FILE_NAME)

with open(full_path, encoding = 'utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count =  int(file.readline())
        ingredients  = []
        for i in range(ingredients_count):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
                "ingredient_name": ingredient_name,
                "quantity": quantity,
                "measure" : measure
            })
        file.readline()   
        cook_book[dish_name] = ingredients
       
print(cook_book)   
    

