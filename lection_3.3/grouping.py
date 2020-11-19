import re

# Для поиска символов можно еще и группировать значения в шаблоне  и для этого используются круглые скобки (), то есть:

# pattern = r'(test)*'
# string = 'test'
# match = re.match(pattern, string)
# print(match)

''' Вывод:
<re.Match object; span=(0, 4), match='test'>'''

# pattern = r'(test)*'
# string = 'testtest'
# match = re.match(pattern, string)
# print(match)

''' Вывод:
<re.Match object; span=(0, 8), match='test'>'''

# Группировка символов чаще всего сопровождается метасимволом " | " - это что-то вроде "или" то есть, если мы указываем
# в группировке  pattern = r'(test|text)*', то мы хотим сказать, найди в строке значения подходящие или под "первую"
# группу символов или под "вторую группу символов". ВАЖНО!!! ПЕРЕД И ПОСЛЕ МЕТАСИМВОЛА " | "  ПРОБЕЛОВ БЫТЬ НЕ ДОЛЖНО

# pattern = r'(test|text)*'
# string = 'testtest'
# match = re.match(pattern, string)
# print(match)

''' Вывод:
<re.Match object; span=(0, 8), match='testtest'>'''


# pattern = r'(test|text)*'
# string = 'text'
# match = re.match(pattern, string)
# print(match)

''' Вывод:
<re.Match object; span=(0, 4), match='text'>'''

# В следующем примере при помощи метода match.groups() мы наглядно можем увидеть, как матч показывает все пересечения :

# pattern = r'((abc)|(test|text)*)'
# string = 'abc'
# match = re.match(pattern, string)
# print(match)
# print(match.groups())

''' Вывод:
<re.Match object; span=(0, 3), match='abc'>
('abc', 'abc', None)'''

# Т.е. в шаблоне pattern = r'((abc)|(test|text)*)' исполняется вот этот  кусок ((abc)|(test|text)*) ---> ('abc'), затем
# ((abc)*) -----> ('abc', 'abc') и в конце исполняется ((test|text)*)-----> ('abc', 'abc', 'None') так как такиого
# пересечения нет


#  Еще один пример для полного понимания

# pattern = r'((abc)|(test|text)*)'
# string = 'testtext'
# match = re.match(pattern, string)
# print(match)
# print(match.groups())

''' Вывод:
<re.Match object; span=(0, 8), match='testtext'>
('testtext', None, 'text')'''


# Следующий пример показывает наглядно как работает нахождение вхождения при помощи метода print(match.group()) То есть
# в предыдущем методе print(match.groups()) выводились все группы шаблона, а в данном примере мы указываем каждую отдельно
# при этом параметром передаем то число, какое мы хотим проверить очередность вхождения например print(match.group(1))
# по умолчанию в методе print(match.group()) указан 0(нуль)

# pattern = r'Hello (abc|test)'
# string = 'Hello abc'
# match = re.match(pattern, string)
# print(match)
# print(match.group(0))
# print(match.group(1))

''' Вывод:
<re.Match object; span=(0, 9), match='Hello abc'>
Hello abc
abc'''


# pattern = r'(\w+)-\1'
# string = 'test-test'
# match = re.match(pattern, string)
# print(match)

''' Вывод:
<re.Match object; span=(0, 9), match='test-test'>'''


# pattern = r'(\w+)-\1'
# string = 'test-test chow-chow'
# match = re.sub(pattern, r'\1',  string)
# print(match)
''' Вывод:
test chow'''


pattern = r'((\w+)-\2)'
string = 'test-test chow-chow'
match = re.findall(pattern,  string)
print(match)
''' Вывод:
[('test-test', 'test'), ('chow-chow', 'chow')]'''
