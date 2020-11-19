import csv
# Чтение файла в CSV формате

# with open('example.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

'''Вывод:
['first name', ' last name', ' module1', ' module2', ' module3', ' description']
['student', ' best', ' 100', ' 100', ' 100', ' Excellent']
['student', ' good', ' 90', '90.2', ' 100', 'Good\nbut could be better']'''

# CSV - Coma Separated Values - Значения разделенные запятыми. То есть что бы все хорошо работало, надо значения
# разделятьт только запятыми, никаких пробелов иначе все будет работать через жопу,так же в данной библиотеке CSV
# у метода csv.reader() есть аогумент delimiter csv.reader(file_name, delimiter=' ')в кавычках мы указываем по какому
# знаку или прочему показателю мы хотим делить значения, то есть \t по табуляции и т.д. по умолчанию стоит ",".
# Однако стоит помнить, что если меняется делиметр - меняется и формат файла, например с CSV на TSV

# Запись файла в формате CSV

students = [
    ['Greg', 'Dean', 70, 80, 90, 'Good job, Greg'],
    ['John', 'Wood', 80, 80.2, 80, 'Nicely done']
]


with open('example.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerows(students)

'''Вывод:
Наш CSV файл был:

first name, last name, module1, module2, module3, description
student,best,100,100,100,Excellent
student,good,90,"90.2",100,"Good
but could be better"

Наш CSV файл стал:

first name, last name, module1, module2, module3, description
student,best,100,100,100,Excellent
student,good,90,"90.2",100,"Good
but could be better"
Greg,Dean,70,80,90,"Good job, Greg"
John,Wood,80,80.2,80,Nicely done'''

# При записи данных в файл в формате CSV пользуемся методом csv.writer(file_name) мы присваиваем его какой-либо
# переменной и затем вызываем у этой переменной новый метод writerows(data_for_appending) при этом стоит помнить, что
# обязательно должно быть указано во множественном числе слово rowS, то есть writerows иначе запись будет производиться
# в неверном формате. Так же стоит помнить, что у метода writer() есть дополнительный аргумент quoting
# writer(file_name, quoting=csv.QUOTE_ALL) по умолчанию задавать значение этого аргумента нет необходимости, однако если
# необходимо взять в кавычки наши данные для записи, то можем указать значение этого аргумента-константой csv.QUOTE_ALL
