import random
import re


def hw_3():
    print("Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X")

    count_of_search_num = 0
    n = abs(int(input("Введите количество элементов в мвссиве:\n")))

    array = [random.randint(1, n) for i in range(0, n)]
    print(*array)

    search_num = abs(int(input(f"Введите число от 1 до {n}\n")))
    if 1 <= search_num <= n:
        for item in array:
            if item == search_num: count_of_search_num += 1
        print(f"Число {search_num} встречается в массиве {count_of_search_num} раз")
    else: print(f"Число {search_num} не находится в диапозоне значений массива")

#     -----------------------------------------------------------------------------------

    print("Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X")

    n_elemets = abs(int(input("Введите количество элементов в мвссиве:\n")))

    array_of_n_elements = [random.randint(1, n_elemets) for i in range(0, n_elemets)]
    print(*array_of_n_elements)

    search_nearest_num = abs(int(input(f"Введите число, по которому будет проведен поиск ближайшего\n")))

    divergence = abs(array_of_n_elements[0] - search_nearest_num)
    memorized_index = 0

    for i in range(len(array_of_n_elements)):
        if abs(array_of_n_elements[i] - search_nearest_num) < divergence:
            divergence = abs(array_of_n_elements[i] - search_nearest_num)
            memorized_index = i

    print(f"Самый близкий элемент равен {array_of_n_elements[memorized_index]}")

#     -----------------------------------------------------------------------------------

    print("Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.")

    eng_dict = {1 : ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'], 2 : ['d', 'g'], 3 : ['b' , 'c', 'm', 'p'], 4 : ['f', 'h', 'v', 'w', 'y'], 5 : ['k'], 8 : ['j', 'x'], 10 : ['q', 'z']}

    rus_dict = {1 : ['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'], 2 : ['д', 'к', 'л', 'м', 'п', 'у'], 3 : ['б', 'г', 'ё', 'ь', 'я'], 4 : ['й', 'ы'], 5 : ['ж', 'з', 'х', 'ц', 'ч'], 8 : ['ш', 'э', 'ю'], 10 : ['ф', 'щ', 'ъ']}

    word = input("Введите слово на английском или на русском\n").lower().replace(' ', '')

    points = 0

    pattern = re.compile("[а-яё]")

    if pattern.findall(word[0]):
        for letter in word:
            for item in rus_dict.items():
                if letter in item[1]:
                    points += item[0]

    else:
        for letter in word:
            for item in eng_dict.items():
                if letter in item[1]:
                    points += item[0]

    print(f"Вы заработали {points} очков")