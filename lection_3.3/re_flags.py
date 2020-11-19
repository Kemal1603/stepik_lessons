import re

# x = re.match(r'text', 'TEXT', re.IGNORECASE)
# print(x)

'''Вывод:
<re.Match object; span=(0, 4), match='TEXT'>'''


x = re.match(r"(te)*?xt", "TEXT", re.IGNORECASE | re.DEBUG)
print(x)
