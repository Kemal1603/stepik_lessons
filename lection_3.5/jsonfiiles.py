import json

student1 = {
    "first_name": "Greg",
    "last_name": "Dean",
    "certificate": True,
    "scores": [70, 80, 90],
    "description": "Good job, Greg",
}

student2 = {
    "first_name": "Wirt",
    "last_name": "Wood",
    "certificate": True,
    "scores": [80, 80.2, 80],
    "description": "Nicely done",
}

data = [student1, student2]
# print(json.dumps(data, indent=4, sort_keys=True))

'''Вывод:
[
    {
        "certificate": true,
        "description": "Good job, Greg",
        "first_name": "Greg",
        "last_name": "Dean",
        "scores": [
            70,
            80,
            90
        ]
    },
    {
        "certificate": true,
        "description": "Nicely done",
        "first_name": "Wirt",
        "last_name": "Wood",
        "scores": [
            80,
            80.2,
            80
        ]
    }
]'''

# Такой вывод позволяет данные в формате Pyhton, выводить в строковом представлении формата json. Этого мы добиваемся
# при помощи команды json.dumps(var_name, indent=0-9, sort_keys=True or False). В методе dumps первым аргументом мы
# принимаем переменную содержащую запись данных в формате Python, второй аргумент-indent отступы, которые мы хотим задать,
# третий аргумент - sort_keys принимает значение True or False в зависимости от того, хотим мы сортировать данные или нет


# Следующий пример, показывает, как мы можем записывать данные в формате json в файл students.json ВАЖНО!!!! Для вывода
# как в первом примере мы используем метод dumpS - S в конце. А для записи используем метод dump без S в конце

# with open('students.json', 'w') as f:
#     json.dump(data, f, indent=4, sort_keys=True)


# Для того, что бы перевести json представление в формат Python используется метотд loads с S в конце. Пример:

# data_json = json.dumps(data, indent=4, sort_keys=True)
# data_again = json.loads(data_json)
# print(data_again)
# print(sum(data_again[0]['scores']))

'''Вывод:
[{'certificate': True,
  'description': 'Good job, Greg', 
  'first_name': 'Greg',
  'last_name': 'Dean', 
  'scores': [70, 80, 90]
  }, 
 {'certificate': True, 
  'description': 'Nicely done',
  'first_name': 'Wirt', 
  'last_name': 'Wood', 
  'scores': [80, 80.2, 80]
  }]

240(Сумма всех баллов первого студента )'''

# Для считывания файла формата json мы используем метод load без S на конце. Пример:

with open('students.json', 'r') as f:
    data_again = json.load(f)
    print(sum(data_again[1]['scores']))


'''Выводо:
240.2(сумма балов второго студента по все предметам)'''
