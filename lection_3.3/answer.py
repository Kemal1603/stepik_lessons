import re

# pattern = r'english?'
# string = 'Do you speak english?'
# match = re.search(pattern, string)
# print(match)

'''Вывод:
<re.Match object; span=(13, 20), match='english'>'''

# Так как "?" - является одним из мета символов, он не попадает в match='english' на выходе, что бы знак вопроса все
# таки попадал в match='english' на выходе, необходимо просто его экранировать при вводе значения шаблона
# pattern = r'english\?'

pattern = r'english\?'
string = 'Do you speak english?'
match = re.search(pattern, string)
print(match)

'''Вывод:
<re.Match object; span=(13, 21), match='english?'>'''
