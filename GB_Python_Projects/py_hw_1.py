def hw_1():
    print("Задача 2: Найдите сумму цифр трехзначного числа.\nВведите число")
    a = int(input())
    print(f"Сумма цифр трехзначного числа {a} = {a // 100 % 10 + a // 10 % 10 + a % 10}")

#     -----------------------------------------------------------------------------------

    print("Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. "
          "Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали "
          "одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?")

#   Петя и Сережа сделали одинаковое количество журавликов, а Катя в 2 раза больше, поэтому сумма всех сделанных
#   журавликов всегда четная, что и следует ожидать от ввода (0, 6, 12, 18 ... )

    total_num = int(input("Введите количество журавликов, кратное 6\n"))
    if total_num % 6 == 0:
        print("%8s %8s %8s\n%8s %8s %8s"
              % ('Петя', 'Катя', 'Сережа', (total_num // 6), (total_num // 6 * 2), (total_num // 6)))
    else: print(f"Число {total_num} не отвечает требованиям задачи")

#     -----------------------------------------------------------------------------------

    print("Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет "
          "с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр "
          "равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется "
          "написать программу, которая проверяет счастливость билета.")

    ticket_num = list(map(int, input("Введите номер билета (6 цифр)\n")))
    if len(ticket_num) == 6:
        print(sum(ticket_num[0:3]) == sum(ticket_num[3:]))
    else: print("Должно быть 6 цифр")

#     -----------------------------------------------------------------------------------

    print("Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается "
          "сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).")

    choc_numb = list(map(int, input(("Введите три числа через пробел (n ,m ,k)\n")).split(' ')))

    print(
        (choc_numb[2] % choc_numb[0] == 0 or choc_numb[2] % choc_numb[1] == 0)
        and choc_numb[2] < choc_numb[0] * choc_numb[1])