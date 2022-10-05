import get_data
import queries

def print_menu():
    print('МЕНЮ')
    print('')
    print('1. Ввести данные из консоли')
    print('2. Загрузить данные из файла .txt')
    print('3. Поиск по справочнику')

def choice(number):
    if number == '1':
        get_data.get_input()
    elif  number == '2':
        get_data.get_file()
    elif  number == '3':
        queries.query_txt(input('Введите значение для поиска: '))
    else:
        print('Некорректный выбор!')

