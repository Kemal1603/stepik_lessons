# x = input().split()
# xs = (int(i) for i in x)

# def even(s):
#     return s % 2 == 0

# evens = filter(even, xs)
# for i in evens:
#     print(i)

#  Функцию def even(s) можно переписать при помощи lambda функций вот так :

# even = lambda s: s % 2 == 0

# И так как мы функцию even используем только лишь раз, когда передаем ее в качестве первого аргумента filter(), то мы
# можем не описывать функцию отдельно, а передать ее сразу первым аргументом:

# evens = filter(lambda s: s % 2 == 0, xs)
# for i in evens:
#     print(i)

#  Лучше всего использовать lambda для использования простых фунций, так как сложные могут принести вред в дальнейшем


a = [
    ('Guido', 'Van', 'Rossum'),
    ('Haskel', 'Curry'),
    ('John', 'Backus')
]


# def length(name):
#     return len(''.join(name))


# name_length = [length(name) for name in a]
# print(name_length)

# В методе sort оказывается есть аргумент key который по умолчанию задан, но его можно менять на свою функцию при
# необходимости и тогда сортировать он будет исходя из параметров вашей функции
# a.sort(key=length)
# print(a)

#  И снова пример с сортировкой имен по количество символов в имени и фамилии можно переписать при помощи lambda

a.sort(key=lambda name: len(''.join(name)))
print(a)
