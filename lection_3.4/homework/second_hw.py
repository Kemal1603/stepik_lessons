import requests
import re
from tldextract import extract
links_list = []
first_link = input()


def all_href_in_link(link_for_check):
    return re.findall(r'<a.*href="([^"]*)', requests.get(link_for_check).text)


for each_link in all_href_in_link(first_link):
    tsd, extracted_domain, tsu = extract(each_link)
    if tsd == '':
        links_list.append(extracted_domain+'.'+tsu)
    else:
        links_list.append(tsd+'.'+extracted_domain+'.'+tsu)

for final_link in sorted(set(links_list)):
    if final_link == '.':
        continue
    else:
        print(final_link)
