import os
import os.path
import shutil

# Узнать какая папака является текущей
print(os.getcwd())

# Перечисление файлов внутри текущей дирректории
print(os.listdir())

#  Проверить существует ли такйо файл
print(os.path.exists('readfile.py'))

#  Так же есть методы, который помогают определить являются ли переданные значения файлами или директориями. Например:
print(os.path.isfile('writefiles.py'))
print(os.path.isdir('homework'))

# Найти абсолютный путь до нашего файла
print(os.path.abspath('osmethod.py'))

#  Сменить текущую деррикторию
# os.chdir('/home/kemal/Desktop/Python')
print(os.getcwd())

#  Генератор os.walk пробегается по всем дирректориям и подпапкам и файлам для поиска
for current_dir, dirs, files in os.walk('.'):
    print(current_dir, dirs, files)

# shutil эта библиотека помогает копировать содержимое одних фалов в другие
shutil.copy('sample.txt', '/home/kemal/Desktop/Python/stepik_lessons/test.txt')

#  shutil.copytree нужен для того что бы копировать целые папки из одних директорий в другие
shutil.copytree('/home/kemal/Desktop/Python/stepik_lessons/lection_2.4', 'lection_2.4/lection_2.4')
