import os
from pprint import pprint
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
            characteristics = {"ingredient_name": ingredient_name, "quantity": int(quantity), "measure" : measure}
            ingredients.append(characteristics)   
        file.readline()
        cook_book[dish_name] = ingredients

# pprint(cook_book, width = 1, sort_dicts = False)        
          
def get_shop_list_by_dishes(dishes, person_count):
    ingredients = dict()

    for dish_name in dishes:  # итерируем список полученных блюд
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:  # итерируем ингридиенты в блюде
                measure_quantity_list = dict()
                if ings['ingredient_name'] not in ingredients:
                    measure_quantity_list['measure'] = ings['measure']
                    measure_quantity_list['quantity'] = ings['quantity'] * person_count
                    ingredients[ings['ingredient_name']] = measure_quantity_list
                else:
                    ingredients[ings['ingredient_name']]['quantity'] = ingredients[ings['ingredient_name']]['quantity'] + ings['quantity'] * person_count
        else:
            print("Вашего блюда нет в списке")                
    return ingredients    

pprint(get_shop_list_by_dishes(['Омлет','Фахитос'], 4), sort_dicts = False)                                                     