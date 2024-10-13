# Напишите функцию print numbers (). Функция должна принимать число и 
# выводить числа в обратном порядке от этого числа до нуля (нуль не выводится).
# По окончании работы функция должна вывести на экран строку Finished


def numbers(num):
    num2 = num
    while num2 > 0:
        print(num2)
        num2 = num2-1
    print("Finished")

numbers(3)
numbers(5)
