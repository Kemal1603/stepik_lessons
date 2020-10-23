lst = [1, 2, 3, 4, 5, 6]
book = {
    'title': 'The Langoliers',
    'author': 'Steven King',
    'year_published': 1990
}

string = 'Hello, World!'

# for i in lst:
#     print(i)
#  Here above is regular for cycle we accepting for in any type of data and iterating that data

# Here below how the FOR cycle is working. There is some special method ITER that is bring all the list and
# give it to the IT variable by part

it = iter(lst)
# a = next(it)
# print(a)
# 1

# try:
#     i = next(it)
# except StopIteration:
#     break
# while True:
#     pass
# This code above doing the same what doing FOR cycle
