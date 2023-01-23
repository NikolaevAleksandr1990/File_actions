with open('recipes.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish = line.strip()
        number_of_ingredients = int(f.readline())
        ingredients = []
        for i in range(number_of_ingredients):
            emp = f.readline().strip()
            ingr, quantity, measure = emp.split(' | ')
            ingredients.append({
                'ingredient_name': ingr,
                'quantity': quantity,
                'measure': measure,
            })
        f.readline()
        cook_book[dish] = ingredients
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingredient in cook_book[dish_name]:
                shop_list[ingredient['ingredient_name']] = \
                    {'quantity': int(ingredient['quantity']) * person_count,
                     'measure': ingredient['measure']}
    return shop_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
