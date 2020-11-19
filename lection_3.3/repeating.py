import re

# Пример с использованием метасимвола "*" - этот метасимвол в шаблоне pattern = r'ab*a' указывает нам на то, что в строке
# мы хотим найти все подходящие элементы с 0 вхождением, то есть слово может начинаться и заканчиваться на "а" при этом
# вторая буква может быть пустой либо может быть сколько угодно символов b, но никаких других символов

# pattern = r'ab*a'
# string = 'aa, aba, abba'
# all_inslusions = re.findall(pattern, string)
# print(all_inslusions)

''' Выод:
['aa', 'aba', 'abba']'''

# Если нам надо хотя бы минимум один и более символов, в этом случае используют знак "+"

# pattern = r'ab+a'
# string = 'aa, aba, abba'
# all_inslusions = re.findall(pattern, string)
# print(all_inslusions)

''' Выод:
['aba', 'abba']'''


# Если мы ищем 0 или максимум одно число вхождений, тогда используется знак "?":

# pattern = r'ab?a'
# string = 'aa, aba, abba'
# all_inslusions = re.findall(pattern, string)
# print(all_inslusions)

''' Выод:
['aa', 'aba']'''


# Если необходимо найти конкретное число вхождений, тогда в фигурных скобках указываем например {3}:

# pattern = r'ab{3}a'
# string = 'aa, aba, abba, abbba, abbbbba'
# all_inslusions = re.findall(pattern, string)
# print(all_inslusions)

''' Выод:
['abbba']'''


# Если мы знаем диапозон от и до скольки вхождений нам надо найти,то мы будем использовать два числа в фигурных скобках:

# pattern = r'ab{2,3}a'
# string = 'aa, aba, abba, abbba, abbbbba'
# all_inslusions = re.findall(pattern, string)
# print(all_inslusions)

''' Выод:
['abba', 'abbba']'''
