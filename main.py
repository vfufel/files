def read_recipes(file_name):
    ''' Запись рецептов в книгу '''
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


def get_shop_list_by_dishes(dishes, person_count):
    ''' Расчет кол-ва ингридентов для блюда'''
    count_ingridients = {}
    cook_book = read_recipes('recipes.txt')

    for dish in dishes:
        if dish in cook_book.keys():
            for values in cook_book[dish]:
                name = values['ingridients_name']
                count = values['quantity']
                unit = values['measure']
                count_dict = {'measure': unit, 'quantity': count * person_count}
                if name in count_ingridients:
                    count_ingridients[name]['quantity'] += count * person_count
                else:
                    count_ingridients[name] = count_dict
        else:
            return f"Одно из блюд отсутвует в книге рецептов"
    return count_ingridients


from pprint import pprint
# pprint(read_recipes('recipes.txt'))

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))