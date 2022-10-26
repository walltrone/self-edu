import os

BASE_DIR = os.getcwd()
LOG_DIR_NAME = 'files'
LOG_FILE_NAME = 'recipes.txt'
file_path = os.path.join(BASE_DIR, LOG_DIR_NAME, LOG_FILE_NAME)


def read_cook_book(file_name):
    with open(file_name, encoding='utf-8') as file:
        cook_book = {}
        for food_recipe in file.read().split('\n\n'):
            name, ingredients_count, *ingredients = food_recipe.split('\n')
            ingredients_list = []
            for ingredient in ingredients:
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredients_list.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[name] = ingredients_list
    return cook_book


def _make_shop_list(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        dish = dish.capitalize()
        if dish in cook_book:
            for ingredients_count in range(len(cook_book[dish])):
                ingredient = cook_book[dish][ingredients_count]
                if ingredient['ingredient_name'] not in shop_list:
                    shop_list[ingredient['ingredient_name']] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    if shop_list:
        return shop_list
    else:
        return 'В поваренной книге нет таких блюд'


def get_shop_list_by_dishes():
    dishes = list(input('Введите блюда в расчете на одного человека' \
                        '(через запятую): ').lower().split(', '))
    person_count = int(input('Введите количество человек: '))
    shop_list = _make_shop_list(dishes, person_count)
    return (shop_list)


cook_book = read_cook_book(file_path)
print(cook_book, sep='\n', end='\n\n')
shop_list = get_shop_list_by_dishes()
print(shop_list)
