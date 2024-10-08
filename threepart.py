#Дано целое число A. Проверить истинность высказывания: «Число A является положительным»

#def logical_one(A):    
#    if A > 0:
#        return True
#    else:
#        return False
#A = int(input("Введите целое число A"))

#logical_one_result = logical_one(A)
#print("Число A является положительным:", logical_one_result)

#Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».

#def logical_two(A):    
#    if A % 2 == 1:
#        return True
#    else:
#        return False
#A = int(input("Введите целое число A"))

#logical_two_result = logical_two(A)
#print("Число A является нечетным»:", logical_two_result)

#Дано целое число A. Проверить истинность высказывания: «Число A является четным».

#def logical_three(A):    
#    if A % 2 == 0:
#        return True
#    else:
#        return False
#A = int(input("Введите целое число A"))

#logical_three_result = logical_three(A)
#print("Число A является четным:", logical_three_result)

#Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A > 2 и B ≤ 3».

#def logical_four(A, B):    
#    if A > 2 and B <= 3:
#        return True
#    else:
#        return False
#A = int(input("Введите целое число A"))
#B = int(input("Введите целое число B"))

#logical_four_result = logical_four(A, B)
#print("Справедливы неравенства A > 2 и B ≤ 3", logical_four_result)

#Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A ≥ 0 или B < −2».

#def logical_five(A, B):    
#    if A >= 0 or B < -2:
#        return True
#    else:
#        return False
#A = int(input("Введите целое число A"))
#B = int(input("Введите целое число B"))

#logical_five_result = logical_five(A, B)
#print("Справедливы неравенства A ≥ 0 или B < −2", logical_five_result)

#Даны три целых числа: A, B, C. Проверить истинность высказывания: «Справедливо двойное неравенство A < B < C».

#def logical_six(A, B, C):    
#    if A < B < C:
#        return True
#    else:
#        return False
#A = int(input("Введите целое число A"))
#B = int(input("Введите целое число B"))
#C = int(input("Введите целое число C"))

#logical_six_result = logical_six(A, B, C)
#print("Справедливо двойное неравенство A < B < C", logical_six_result)

#Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B находится между числами A и C».

#def logical_seven(A, B, C):    
#    if A < B < C or C < B < A:
#        return True
#    else:
#        return False
#A = int(input("Введите целое число A"))
#B = int(input("Введите целое число B"))
#C = int(input("Введите целое число C"))

#logical_seven_result = logical_seven(A, B, C)
#print("Число B находится между числами A и C", logical_seven_result)

#Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел A и B нечетное».

#def logical_eight(A, B):    
#    if A % 2 == 1 and B % 2 == 1:
#        return True
#    else:
#        return False
#A = int(input("Введите целое число A"))
#B = int(input("Введите целое число B"))

#logical_eight_result = logical_eight(A, B)
#print("Каждое из чисел A и B нечетное", logical_eight_result)

#Даны два целых числа: A, B. Проверить истинность высказывания: «Хотя бы одно из чисел A и B нечетное».

#def logical_nine(A, B):    
#    if A % 2 == 1 or B % 2 == 1:
#        return True
#    else:
#        return False
#A = int(input("Введите целое число A"))
#B = int(input("Введите целое число B"))

#logical_nine_result = logical_nine(A, B)
#print("Хотя бы одно из чисел A и B нечетное", logical_nine_result)

#Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное»

#def logical_ten(A, B):    
#    if (A % 2 == 1 and B % 2 == 0) or (A % 2 == 0 and B % 2 == 1):
#        return True
#    else:
#        return False
#A = int(input("Введите целое число A"))
#B = int(input("Введите целое число B"))

#logical_ten_result = logical_ten(A, B)
#print("Ровно одно из чисел A и B нечетное", logical_ten_result)
