#Найдите и скопируйте алгоритм бинарного поиска. Запустите код и попробуйте разобраться как он работает
#Бинарный поиск — это эффективный алгоритм поиска элемента в отсортированном массиве (списке). Он работает, разделяя список на половины, что значительно сокращает количество шагов по сравнению с линейным поиском.

#Алгоритм бинарного поиска:
#Сначала алгоритм сравнивает целевой элемент с элементом в середине списка.
#Если целевой элемент меньше, поиск продолжается в левой половине.
#Если целевой элемент больше, поиск продолжается в правой половине.
#Этот процесс повторяется до тех пор, пока элемент не будет найден или пока подсписок не станет пустым.

# Функция бинарного поиска
def binary_search(arr, target): #arr массив, target искомый элемент
    left = 0  # Начало списка(диапазона)
    right = len(arr) - 1  # Конец списка(диапазона)

    while left <= right: #Повторяем следующие шаги пока диапазон не пустой
        mid = (left + right) // 2  # считаем индекс Среднего элемента

        # Если элемент найден
        if arr[mid] == target: 
            return mid #возращаем номер среднего
        
        # Если целевой элемент меньше среднего, ищем в левой половине
        elif arr[mid] > target:
            right = mid - 1 # оставляем правую сторону
        
        # Если целевой элемент больше среднего, ищем в правой половине
        else:
            left = mid + 1 # оставляем левую сторону

    # Если элемент не найден
    return -1 #если нет в массиве вернуть -1

# Пример использования бинарного поиска
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] #отсортированный список
target = 7 #искомый элемент

# Запуск поиска
result = binary_search(sorted_list, target)

# Проверка результата
if result != -1:
    print(f"Элемент найден на позиции: {result}") #Если index не равен -1, то элемент найден, выводится сообщение.
else:
    print("Элемент не найден") #Если index равен -1, то элемент не найден, выводится сообщение.


#Найдите и скопируйте алгоритм пузырьковой сортировки. Запустите код и попробуйте разобраться как он работает
#Пузырьковая сортировка - это простой алгоритм сортировки, который работает, сравнивая соседние элементы и меняя их местами, если они расположены в неправильном порядке.
#Процесс повторяется, пока все элементы не окажутся в правильном порядке.

def bubble_sort(arr):
    n = len(arr)
    # Внешний цикл проходит по всем элементам массива
    for i in range(n):
        # Внутренний цикл сравнивает соседние элементы
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Пример использования функции
arr = [64, 34, 25, 12, 22, 11, 90]
print("Исходный массив:", arr)
bubble_sort(arr)
print("Отсортированный массив:", arr)


