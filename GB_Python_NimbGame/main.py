# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def binary_search():
    array = [i for i in range(100)]
    left = 0
    right = len(array) - 1
    middle = (left + right) // 2

    while left <= right:
        middle = (left + right) // 2
        answer = input(f'Это число больше {array[middle]}? -- ')
        if answer.lower() == 'да':
            left = middle + 1
        elif answer.lower() == 'нет':
            left = middle - 1
        else:
            print('Вы ответили неверно. Укажите "да" или "нет"')
        print(array[middle])

def bubble_sort():
    array = [random.randrange(1, 50, 1) for i in range(10)]
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    print(array)

def nim_game():
    n = int(input("Введите количество камней в куче ? -- "))
    count = 1

    while n > 0:
        count = count + 1
        if count % 2 == 0:
            comp = random.randint(1, 3)
            print(f'Компьютер взял {comp} камней')
            n = n - comp
            print(f'Количество камней осталось {n}')
            if n <= 0:
                print('Компьютер победил!')
        else:
            player = int(input('Введите количество камней (от 1 до 3): '))
            while player < 1 or player > 3:
                print('Вы ошиблись!')
                player = int(input('Введите количество камней (от 1 до 3): '))
                n = n - player
                print(f'Количество камней осталось {n}')
                if n <= 0:
                    print('Вы победили!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    binary_search()
    bubble_sort()
    nim_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
