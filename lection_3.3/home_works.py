# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
#
# Примечание:
# Считать все строки по одной из стандартного потока ввода вы можете, например, так
#
# import sys
#
# for line in sys.stdin:
#     line = line.rstrip()
#     # process line
#
# Sample Input:
#
# catcat
# cat and cat
# catac
# cat
# ccaatt
# Sample Output:
#
# catcat
# cat and cat

# put your python code here
# import re
# import sys
# pattern = r'((cat).*){2,}'
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(pattern, line):
#         print(line)


# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.
#
# Примечание:
# Для работы со словами используйте группы символов \b и \B.
# Описание этих групп вы можете найти в документации.
# Sample Input:
#
# cat
# catapult and cat
# catcat
# concat
# Cat
# "cat"
# !cat?
# Sample Output:
#
# cat
# catapult and cat
# "cat"
# !cat?
#
#
#
# # put your python code here
# import re
# import sys
# pattern = r'\bcat\b'
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(pattern, line):
#         print(line)

# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
# Sample Input:
#
# zabcz
# zzz
# zzxzz
# zz
# zxz
# zzxzxxz
# Sample Output:
#
# zabcz
# zzxzz


# put your python code here
# import re
# import sys
# pattern = r'z\w{3}z'
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(pattern, line):
#         print(line)


# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\﻿".
# Sample Input:
#
# \w denotes word character
# No slashes here
# Sample Output:
#
# \w denotes word character

# put your python code here
# import re
# import sys
# pattern = r'\\'
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(pattern, line):
#         print(line)


# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
#
# Sample Input:
#
# blabla is a tandem repetition
# 123123 is good too
# go go
# aaa
# Sample Output:
#
# blabla is a tandem repetition
# 123123 is good too

# put your python code here
# import re
# import sys
# pattern = r'\b(.+)\1\b'
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(pattern, line):
#         print(line)

# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.
#
# Sample Input:
#
# I need to understand the human mind
# humanity
# Sample Output:
#
# I need to understand the computer mind
# computerity

# put your python code here
# import re
# import sys
#
# pattern = r'human'
#
# for line in sys.stdin:
#     print(re.sub(pattern, 'computer', line.rstrip()))



# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".
#
# Примечание:
# Обратите внимание на параметр count у функции sub.
# Sample Input:
#
# There’ll be no more "Aaaaaaaaaaaaaaa"
# AaAaAaA AaAaAaA
# Sample Output:
#
# There’ll be no more "argh"
# argh AaAaAaA
#
# import sys
# import re
#
# for line in sys.stdin:
#     line = re.sub(r"\ba+\b", "argh", line.rstrip(), 1, flags=re.IGNORECASE)
#     print(line)


# Вам дана последовательность строк.
# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.
# Sample Input:
#
# this is a text
# "this' !is. ?n1ce,
# Sample Output:
#
# htis si a etxt
# "htis' !si. ?1nce,


# put your python code here
# import re
# import sys
# pattern = r'human'
#
# for line in sys.stdin:
#     print( re.sub(r'(\w)(\w)(\w*)', r'\2\1\3', line.rstrip()))


# Вам дана последовательность строк.
# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.
# Sample Input:
#
# attraction
# buzzzz
# Sample Output:
#
# atraction
# buz
#
#
# # put your python code here
# import re
# import sys
#
# pattern = r'human'
#
# for line in sys.stdin:
#     print( re.sub(r"(\w)(\1)+", r"\1", line.rstrip()))
