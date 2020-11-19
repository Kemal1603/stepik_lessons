#  Первый вариант  не верный

# import requests
# import re
# links_list = []
# first_link = input()
# second_link = input()
#
#
# def all_href_in_link(link_for_check):
#     return re.findall(r'<a.*href="([^"]*)', requests.get(link_for_check).text)
#
#
# def links_checker(links):
#     for link in links:
#         if link.startswith('h'):
#             return link
#
#
# links_list.append(links_checker(all_href_in_link(first_link)))
# inner_links = []
#
# for each_link in links_list:
#     inner_links.append(links_checker(all_href_in_link(each_link)))
# print(links_list)
# print(inner_links)
# if second_link in inner_links:
#     print('Yes')
# else:
#     print('No')


# Второй вариант верный

"""A = input()
B = input()
pattern = r'http.*html'
list_urlA = re.findall(pattern, requests.get(A).text)
list_url = []
for url in list_urlA:
    list_url += re.findall(pattern, requests.get(url).text)
print(list_urlA)
print(list_url)
if B in list_url:
    print('Yes')
else:
    print('No')"""

