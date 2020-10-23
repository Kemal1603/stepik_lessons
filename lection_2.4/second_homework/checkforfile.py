import os.path
from itertools import groupby
lst = []
os.chdir('/home/kemal/Downloads')

for current_dir, dirs, files in os.walk('.'):
    for file_name in files:
        if '.py' in file_name:
            lst.append(current_dir.lstrip('./'))

new_lst = [el for el, _ in groupby(lst)]
del new_lst[0]

with open('/home/kemal/Downloads/a.txt', 'w') as f:
    content = '\n'.join(sorted(new_lst))
    f.write(content)


# Пример якобы правильного решения
# import os
#
# for cur_dir, subdirs, files in os.walk("main"):
#     for file in files:
#         if file.endswith(".py"):
#             print(cur_dir)
#             break
