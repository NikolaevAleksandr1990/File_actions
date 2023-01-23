with open('recipes.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish = line.strip()
        number_of_ingredients = int(f.readline())
        ingredients = []
        for i in range(number_of_ingredients):
            emp = f.readline().strip()
            ingredient, quantity, measure = emp.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient,
                'quantity': quantity,
                'measure': measure,
            })
        f.readline()
        cook_book[dish] = ingredients
print(cook_book)