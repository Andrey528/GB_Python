def hw_6(random_array):
    print("Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.")

    start_num = int(input("Введите первый элемент прогрессии:\n"))
    step = int(input("Введите шаг прогрессии:\n"))
    reg_len = int(input("Введите количество элементов прогрессии:\n"))

    array = [start_num + (i - 1) * step for i in range(1, reg_len + 1)]
    print('\n'.join(map(str, array)))

#     -----------------------------------------------------------------------------------

    print("Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)")

    user_range = list(map(int, input("Введите диапозон через пробел:\n").split(' ')))
    index_list = []

    if len(user_range) != 2 and user_range[1] <= user_range[0]:
        return print("Некорректный ввод")

    print(random_array)

    for i in range(len(random_array)):
        if user_range[0] <= random_array[i] <= user_range[1]:
            index_list.append(i)

    print(index_list)