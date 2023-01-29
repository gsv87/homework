import json
from prettytable import PrettyTable

file_json = 'data.json'
# Куда сохранем и откуда загружаем словарь с данными сотрудников
file_txt = 'result.txt'
# Куда сохранем результаты поиска
input_data = {'age': 'возраст', 'post': 'должность', 'telephone': 'телефон'}
keys = ['age', 'post', 'telephone']
values = [input_data[i] for i in keys]
# Оба списка для того чтобы не было рандома при вводе и выводе информации,
# а все шло по порядку: возраст, должность, телефон
search_option = {'find': ['фамилию', 'фамилии'],
                 'finda': ['возраст', 'возрасту'],
                 'finds': ['первую букву фамилии', 'первой букве фамилии']}
# Для универсальности ввода и вывода данных и сохранения результатов поиска

# На всякий случай оставил список, вдруг json файл потеряется
# s = {'Ivanov': {'age': '25', 'post': 'manager', 'telephone': '88005552222'},
#      'Dmitriev': {'age': '27', 'post': 'economist', 'telephone': '88005553333'},
#      'Sidorov': {'age': '29', 'post': 'office manager', 'telephone': '88005554444'},
#      'Sokolov': {'age': '23', 'post': 'manager', 'telephone': '88005551234'},
#      'Matveev': {'age': '27', 'post': 'IT specialist', 'telephone': '88005554421'},
#      'Karpov': {'age': '28', 'post': 'deputy dir', 'telephone': '88005552345'},
#      'Somov': {'age': '34', 'post': 'director', 'telephone': '88005557866'},
#      'Petrov': {'age': '36', 'post': 'logistics', 'telephone': '88005551126'},
#      'Makarov': {'age': '34', 'post': 'IT specialist', 'telephone': '88005554422'},
#      'Isaev': {'age': '30', 'post': 'office manager', 'telephone': '88005556655'},
#      'Popov': {'age': '28', 'post': 'manager', 'telephone': '88005557733'}}
#
# with open(file=file_json, mode='w') as file_output:
#     json.dump(s, file_output, indent=3)


def data_entry(name: str):
    """ Функция для редактирования и добавления новых сотрудников
    """
    s[name] = {}
    for key in keys:
        s[name][key] = input(f'Введите {input_data[key]}: ')


def output_employee_information(names: list):
    """ Функция для вывода информации по списку сотрудников
    """
    # Передаем в PrettyTable() имена заголовков столбцов
    # Про prettytable особо ни чего не знаю, просто нашел как сделать таблицу,
    # чтобы вывод был покрасивей
    new_table = PrettyTable(['сотрудник'] + values)
    for i in names:
        new_table.add_row([i, s[i].get(keys[0], "unknown"), s[i].get(keys[1], "unknown"), s[i].get(keys[2], "unknown")])
    print(new_table)


def search_employees(command: str):
    """ Функция поиска сотрудников в зависимости от параметра command.
    Если command = 'find' то поиск по фамилии, если 'finda' - поиск по возрасту
    и если 'finds' - поиск по первой букве фамилии. Возвращает список найденных
    сотрудников или пустой список если таковых нет и значение поиска
    """
    request = input(f'Введите {search_option[command][0]} сотрудника для поиска: ')
    if command == 'find':
        result = [i for i in s.keys() if i == request]
    elif command == 'finda':
        result = [i for i in s.keys() if s[i]['age'] == request]
    else:
        result = [i for i in s.keys() if i[0] == request]
    return result, request


def save_search_results(spisok, command=None, request=''):
    """ Функция сохраняет в текстовый файл, данные сотрудников из списка spisok.
    """
    while True:
        otvet = input('Сохранить результат в текстовый файл? (yes/no): ')
        if otvet == 'no':
            print('Данные не сохранены')
            break
        elif otvet == 'yes':
            if command is not None:
                result = f'Результаты поиска сотрудников по {search_option[command][1]} - "{request}":\n'
            else:
                result = 'Список всех сотрудников:\n'
            for i in spisok:
                # В f'' строке ниже в фигурные скобки после имени переменной
                # добавил :<30 чтобы были отступы межды столбцами
                result += f'{i:<20} ' \
                            f'{s[i].get(keys[0], "unknown"):<10} ' \
                            f'{s[i].get(keys[1], "unknown"):<30} ' \
                            f'{s[i].get(keys[2], "unknown")}\n'
            with open(file=file_txt, mode='w', encoding='UTF-8') as f:
                f.write(result)
                print(f'Данные сохранены в файл {file_txt}')
            break
        else:
            print('Не верный ввод')


def save_data_to_json():
    """ Функция сохраняет все данные сотрудников в файл json
    """
    with open(file=file_json, mode='w') as file_output:
        json.dump(s, file_output, indent=3)
        print(f'Список сотрудников сохранен в файл {file_json}')


def staff_members():
    """ Информационная система Сотрудники. Доступны команды:
    add - Добавление сотрудника
    replace - Изменение данных сотрудника
    delete - Удаление сотрудника
    find - Поиск сотрудника по фамилии
    finda - Поиск сотрудников указанного возраста
    finds - Поиск сотрудников фамилии которых начинаются на указанную букву
    all - Вывод всех сотрудников
    save - Сохранение данных словаря в файл
    help - Справка по доступным командам
    exit - Выход из программы
    """
    print(staff_members.__doc__)
    command = input('Введите команду (add/replace/delete/find/finda/finds/all/save/help/exit): ')
    while True:
        if command == 'add':
            last_name = input('Введите фамилию: ')
            if last_name not in s.keys():
                data_entry(last_name)
                print(f'Сотрудник {last_name} создан')
            else:
                print(f'Сотрудник {last_name} уже есть в списке')

        elif command == 'replace':
            last_name = input('Введите фамилию: ')
            if last_name in s.keys():
                data_entry(last_name)
                print(f'Сотрудник {last_name} изменен')
            else:
                print(f'Сотрудника {last_name} нет в списке')

        elif command == 'delete':
            last_name = input('Введите фамилию: ')
            if last_name in s.keys():
                del s[last_name]
                print(f'Сотрудник {last_name} успешно удален')
            else:
                print('Такого сотрудника нет!!')

        elif command in ('find', 'finda', 'finds'):
            result, request = search_employees(command)
            if result:
                output_employee_information(result)
                save_search_results(result, command, request)
            else:
                print('Сотрудники не найдены')

        elif command == 'all':
            list_all = [i for i in s.keys()]
            output_employee_information(list_all)
            save_search_results(list_all)

        elif command == 'save':
            save_data_to_json()

        elif command == 'help':
            print(staff_members.__doc__)

        elif command == 'exit':
            save_data_to_json()
            print('Пока')
            break

        else:
            print('Введите допустимую команду! (add/replace/delete/find/finda/finds/all/save/help/exit)')

        command = input('Введите команду (add/replace/delete/find/finda/finds/all/save/help/exit): ')


if __name__ == '__main__':
    try:
        with open(file=file_json, mode='r') as r:
            s = json.load(r)
    except FileNotFoundError:
        print(f'Файл {file_json} не найден')
        if input('Создать пустой словарь? (yes/no) ') == 'yes':
            s = {}
            staff_members()
        else:
            print('Нет так нет')
    else:
        print(f'Данные из файла {file_json} загружены')
        staff_members()
