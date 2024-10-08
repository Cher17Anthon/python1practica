#Дано расстояние L в сантиметрах. Используя операцию деления нацело, найти количество полных метров в нем (1 метр = 100 см).

#def metre (L):
#    return L // 100
#L = int(input("Введите расстояние L в сантиметрах"))
#metreL = metre(L)
#print("расстояние L в метрах:", metreL)

#Дана масса M в килограммах. Используя операцию деления нацело, найти количество полных тонн в ней (1 тонна = 1000 кг).

#def tonne (M):
#    return M // 1000
#M = int(input("Введите массу M в килограммах"))
#tonneM = tonne(M)
#print("масса M в тоннах:", tonneM)

#Дан размер файла в байтах. Используя операцию деления нацело, найти количество полных килобайтов, которые занимает данный файл (1 килобайт = 1024 байта).

#def kilobytes (K):
#    return K // 1024
#K = int(input("Введите размер файла K в байтах"))
#tonneK = kilobytes(K)
#print("размер файла K в килобайт:", tonneK)

#Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений). Используя операцию деления нацело, найти количество отрезков B, размещенных на отрезке A.
#A = int(input("Введите длину отрезка A: "))
#B = int(input("Введите длину отрезка B: "))

#def count_segments(A, B):
#    if A < B:
#        return 0
#    else:
#        return A // B
    
#quantity = count_segments(A, B)
#print("Количество отрезков B =", quantity)

#Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений). Используя операцию взятия остатка от деления нацело, найти длину незанятой части отрезка A.

#A = int(input("Введите длину отрезка A: "))
#B = int(input("Введите длину отрезка B: "))

#def count_remains(A, B):
#    if A < B:
#        return 0
#    else:
#        return A % B
#remains = count_remains(A, B)
#print("Количество незанятой части", remains)

#Дано двузначное число. Вывести вначале его левую цифру (десятки), а затем — его правую цифру (единицы). Для нахождения десятков использовать операцию деления нацело, для нахождения единиц — операцию взятия остатка от деления.

#def two_number(number):
#    ten = number // 10
#    ten_remains = number % 10
#    return ten, ten_remains
#number = int(input("Введите двузначное число: "))

#if 10 <= number <= 99:
#   ten, ten_remains = two_number(number)
#    print("левая цифра (десятки)", ten)
#    print("правая цифра (единицы)", ten_remains)
#else:
#    print("Ошибка: Число не  двузначное")

#Дано двузначное число. Найти сумму и произведение его цифр.

#def two_number(number):
#    ten = number // 10
#    ten_remains = number % 10
#    sum = ten + ten_remains
#    multi = ten * ten_remains
#    return sum, multi

#number = int(input("Введите двузначное число: "))

#if 10 <= number <= 99:
#    sum, multi = two_number(number)
#    print("сумма цифр", sum)
#    print("произведение цифр", multi)
#else:
#    print("Ошибка: Число не  двузначное")

#Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа.
#def two_number(number):
#    ten = number // 10
#    ten_remains = number % 10
#    reverse = ten_remains * 10 + ten
#    return reverse

#number = int(input("Введите двузначное число: "))

#if 10 <= number <= 99:
#    reverse = two_number(number)
#    print("Число с переставленными цифрами:", reverse)
#else:
#    print("Ошибка: Число не  двузначное")

#Дано трехзначное число. Используя одну операцию деления нацело, вывести первую цифру данного числа (сотни).

#def three_number(number):
#    hundred = number // 100
#    return hundred
#number = int(input("Введите трехзначное число: "))

#if 100 <= number <= 999:
#    hundred = three_number(number)
#    print("первая цифра (сотни)", hundred)
#else:
#    print("Ошибка: Число не трехзначное число")

#Дано трехзначное число. Вывести вначале его последнюю цифру (единицы), а затем — его среднюю цифру (десятки).

#def three_number(number):
#    units = number // 100
#    dozen = (number // 10) % 10
#    return units, dozen
#number = int(input("Введите трехзначное число: "))

#if 100 <= number <= 999:
#    units, dozen = three_number(number)
#    print("последняя цифра (единицы)", units)
#    print("средняя цифра (десятки)", dozen)
#else:
#    print("Ошибка: Число не трехзначное число")
