# import requests
# import json
#
# with open('/home/kemal/Downloads/dataset_24476_3.txt', 'r') as file:
#     for input_int in file.readlines():
#         url = f'http://numbersapi.com/{input_int.rstrip()}/math'
#         respond_from_service = requests.get(url, params={'json': True})
#         converted_from_json = json.loads(respond_from_service.text)
#         if converted_from_json['found']:
#             print('Interesting')
#         else:
#             print('Boring')


