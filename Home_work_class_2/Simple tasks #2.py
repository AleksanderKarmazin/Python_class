# BorisRubin
# http://codegists.com/snippet/python/hw_day2_mainpy_borisrubin_python

# Создать лист из 6 любых чисел. Отсортировать его по возрастанию
print('ЗАДАЧА 1: Создать лист из 6 любых чисел. Отсортировать его по возрастанию\n')
numbers = [1, 22, 23, 0.19, 1802, -2]
print('Исходный список ', numbers)
numbers.sort()
print('Сортировка "по возрастанию" ', numbers)
 
 
 
# Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно
print('\n\nЗАДАЧА 2: Создать словарь из 5 пар: int -> str, например {6: \'6\'}, вывести его в консоль попарно\n')
dict = {1:'first', 12:'twelwe', 5:'five', 6:'six', 20:'twenty'}
print('Исходный словарь', dict)
 
for key, value in dict.items():
    print(key, value)
 
 
 
# Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем
print('\n\nЗАДАЧА 3: Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем\n')
tuple_1 = (1.2, 0.21, 32.1, 5.5, 8.9, 2.13, 3.1415, 0.001, 12122.1, 7.5)
print('Максимальное значений в Tuple ', max(tuple_1))
print('Минимальное значений в Tuple ', min(tuple_1))
 
 
 
# Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку, чтобы получилось: 'Earth -> Russia -> Moscow'
print('\n\nЗАДАЧА 4: Создать лист из 3 слов: [\'Earth\', \'Russia\', \'Moscow\'], соеденить все слова в единую строку, чтобы получилось: \'Earth -> Russia -> Moscow\'\n')
words = ['Earth', 'Russia', 'Moscow']
print(" -> ".join(words))
 
# Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
print('\n\nЗАДАЧА 5: Взять строку \'/bin:/usr/bin:/usr/local/bin\' и разбить ее в список по символу \':\'')
string = '/bin:/usr/bin:/usr/local/bin'
print(string.split(':'))
 
 
 
# Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет
print('\n\nЗАДАЧА 6: Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет')
print([i for i in range(1,100) if i%7 == 0])
 
 
# Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы
print('\n\nЗАДАЧА 7: Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы')
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9],
          [10,11,12]]
 
print('Выводим строки\n')
for col in range(len(matrix)):
    print('\n')
    for string in range(len(matrix[col])):
        print(matrix[col][string], end = ' ')
 
print('Выводим колонки\n')
for string in range(len(matrix[col])):
    print('\n')
    for col in range(len(matrix)):
        print(matrix[col][string], end = ' ')
 
 
 
 
# Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс
print('\n\nЗАДАЧА 8: Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс')
obj = [1, 'fix', False, None, {1:'dict'}, (5,6,7)]
for i in obj:
    print(i, ' ', obj.index(i))
 
 
 
# Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'
print('\n\nЗАДАЧА 9: Создать список с тремя значениями \'to-delete\' и нескольми любыми другими, удалить из него все значения \'to-delete\'')
some_data = ['to-delete','1','to-delete','2','3','4','to-delete','5']
print('Список данных до чистки: ', some_data)
some_data = [data for data in some_data if data !='to-delete']
print('Список данных после чистки: ', some_data)
 
 
 
# Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль
print('\n\nЗАДАЧА 10: Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль')
for i in range(10,0,-1):
    print(i, end = ' ')
 
print('\n')