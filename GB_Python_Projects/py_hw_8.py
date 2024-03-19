def read_csv_or_txt(path, fields):
    data =[]

    with open(path) as f:
        [data.append(dict(zip(fields, line.replace('\n', '').split(',')))) for line in f.readlines()]
    return data

def show_menu():
    user_input = int(input("Введите номер пункта меню:\n"
          "1. Вывести телефонный справочник\n"
          "2. Поиск в справочнике по фамилии\n"
          "3. Поиск в справочнике по номеру\n"
          "4. Добавить новые данные в справочник\n"
          "5. Сохранить данные в txt\n"
          "6. Изменить данные\n"
          "7. Удалить данные\n"
          "8. Завершение работы\n"))
    print()
    return user_input

def print_result(data):
    [print("%8s" % (key), end='\t') for key in data[0].keys()]
    print('\n----------------------------------------------------------')
    for line in data:
        [print("%8s" % (value), end='\t') for value in line.values()]
        print()
    print('----------------------------------------------------------\n')

def choose_in_data(data, fields):
    if data == {}:
        print("Не из чего выбирать")
    dict_of_dicts = {}
    print(*fields)
    for dicts in data:
        for i in range(0, len(data)):
            print(f"{i})", end='\t')
            [print(f"{value}", end='\t') for value in dicts.values()]
            print()
            dict_of_dicts[i] = dicts
    # print(dict_of_dicts)
    user_input = int(input("Введите номер строки данных, которую хотите изменить\n"))
    return user_input

def choose_search_field():
    user_flag = int(input("Введите номер критерия для поиска:\n"
          "1. Фамилия\n"
          "2. Имя\n"
          "3. Телефон\n"
          "4. Описание\n"))
    if user_flag == 1:
        search_flag = 'Фамилия'
    elif user_flag == 2:
        search_flag = 'Имя'
    elif user_flag == 3:
        search_flag = 'Телефон'
    elif user_flag == 4:
        search_flag = 'Описание'
    return search_flag

def get_search_by_something(search_flag):
    if search_flag == 'Фамилия':
        user_input = input("Введите фамилию для поиска:\n").lower()
    elif search_flag == 'Имя':
        user_input = input("Введите имя для поиска:\n").lower()
    elif search_flag == 'Телефон':
        user_input = input("Введите номер для поиска:\n")
    elif search_flag == 'Описание':
        user_input = input("Введите описание для поиска:\n").lower()
    return user_input

def find_by_something(data, flag, search_item):
    try:
        result = list(filter(lambda x: x.get(flag).lower() == search_item, data))
    except:
        result = []
    return result

def get_new_user():
    user_info = list(input("Введите новые данные через запятую без пробела (Фамилия,Имя,Номер,Описание)\n").split(','))
    return user_info

def add_user(phone_book, fields, user_info):
    phone_book.append(dict(zip(fields, user_info)))
    return phone_book

def write_txt_or_csv(path, data):
    with open(path, 'w') as f:
        for line in data:
            [f.write(value + ',') for value in line.values()]
            f.write('\n')

def what_field_to_change():
    user_input = int(input("Что хотите изменить в данных?\n"
          "1. Фамилия\n"
          "2. Имя\n"
          "3. Телефон\n"
          "4. Описание\n"
          "5. Выйти\n"))
    return user_input

def find_row_in_data(data, row):
    i = 0
    for rows in data:
        if str(row) == str(rows):
            index = i
        i += 1
    return index

def change_row(data, changin_row, fields):
    user_input = what_field_to_change()
    index = find_row_in_data(data, changin_row)
    while user_input != 5:
        [print(key, ":", value) for key, value in data[index].items()]
        data[index][fields[user_input - 1]] = input("Введите новое значение:\n")
        user_input = what_field_to_change()
    return data

def delete_row(data, delete_row):
    index = find_row_in_data(data, delete_row)
    data.pop(index)
    return data

def work_with_phonebook():
    choice = show_menu()
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    phone_book = read_csv_or_txt('phonebook.csv', fields)

    while (choice != 8):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            suname = get_search_by_something('Фамилия')
            result = find_by_something(phone_book, 'Фамилия', suname)
            if result != []:
                print_result(result)
            else:
                print("Поиск не дал результата")

        elif choice == 3:
            number = get_search_by_something('Телефон')
            result = find_by_something(phone_book, 'Телефон', number)
            if result != []:
                print_result(result)
            else:
                print("Поиск не дал результата")
        elif choice == 4:
            user_data = get_new_user()
            print(user_data)
            phone_book = add_user(phone_book, fields, user_data)
            file_name = 'phonebook.csv'
            write_txt_or_csv(file_name, phone_book)
        elif choice == 5:
            file_name = 'phon.txt'
            write_txt_or_csv(file_name, phone_book)
        elif choice == 6:
            search_flag = choose_search_field()
            search_item = get_search_by_something(search_flag)
            result = find_by_something(phone_book, search_flag, search_item)
            if result != []:
                user_input = choose_in_data(result, fields)
                phone_book = change_row(phone_book, result[user_input], fields)
                file_name = 'phonebook.csv'
                write_txt_or_csv(file_name, phone_book)
            else:
                print("Поиск не дал результата")
        elif choice == 7:
            search_flag = choose_search_field()
            search_item = get_search_by_something(search_flag)
            result = find_by_something(phone_book, search_flag, search_item)
            if result != []:
                user_input = choose_in_data(result, fields)
                phone_book = delete_row(phone_book, result[user_input])
                file_name = 'phonebook.csv'
                write_txt_or_csv(file_name, phone_book)
            else:
                print("Поиск не дал результата")
        choice = show_menu()

def hw_8():
    work_with_phonebook()