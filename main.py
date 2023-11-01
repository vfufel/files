def read_recipes(file_name):
    cook_book = {}
    recipes = []
    index = 0
    recipes_fix = []
    with open(file_name, encoding='UTF-8') as file:
        lines = file.readlines()
    for idx, element in enumerate(lines):
        if element == '\n':
            recipes.append(lines[index:idx])
            index = idx + 1
        elif idx == len(lines) - 1:
            recipes.append(lines[index:idx + 1])
    for elements in recipes:
        new_elements = [element.rstrip() for element in elements]
        recipes_fix.append(new_elements)
    for recipe in recipes_fix:
        cook_book.update({recipe[0]: []})
        for ingridient in recipe[2:]:
            parts = ingridient.split('|')
            name = parts[0].strip()
            count = int(parts[1].strip())
            unit = parts[2].strip()
            ingridients = {'ingridients_name': name, 'quantity': count, 'measure': unit}
            cook_book[recipe[0]].append(ingridients)
    return cook_book

# from pprint import pprint
# pprint(read_recipes('recipes.txt'))

print(read_recipes('recipes.txt'))