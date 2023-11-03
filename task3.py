def reading_files():
    ''' Считка с файлов в переменную'''
    name_files = ['1.txt', '2.txt', '3.txt']
    full_text = {}

    for name in name_files:
        with open(name, encoding='UTF-8') as file:
            lines = file.readlines()
            len_files = len(lines)
            full_text[len_files] = lines
            full_text[len_files].insert(0, name + '\n')
            full_text[len_files].insert(1, str(len_files) + '\n')
    return full_text


def sort_keys():
    ''' Сортировка ключей '''
    text = reading_files()
    keys = list(text.keys())
    keys.sort()

    return keys

def write_on_file():
    ''' Очистка и запись в новый файл '''
    text = reading_files()
    keys = sort_keys()
    with open('merged_file.txt', mode='w', encoding='UTF-8') as file:
        file.write(' ')

    with open('merged_file.txt', mode='a', encoding='UTF-8') as file:
        for key in keys:
            for line in text[key]:
                file.write(line)

def reading_new_file(name):

    with open('merged_file.txt', mode='r', encoding='UTF-8') as file:
        return file.readlines()


from pprint import pprint
write_on_file()
pprint(reading_new_file('merged_file.txt'))
