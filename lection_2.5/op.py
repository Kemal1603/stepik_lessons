import operator as op

# print(op.add(4, 5))
# print(op.mul(4, 5))
# print(op.contains([1, 2, 3], 4))

# x = [1, 2, 3]
# f = op.itemgetter(1)
# print(f(x))
#  Код выше делает, что-то вроде index OF


a = [
    ('Guido', 'Van', 'Rossum'),
    ('Haskel', 'Curry'),
    ('John', 'Backus')
]

a.sort(key=op.itemgetter(-1))
print(a)

#  Код выше сортирует спикок кортежей по второму элементу, то есть сортирует по фамилиям в алфавитном порядке
