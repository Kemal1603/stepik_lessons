import csv
from collections import Counter

list_of_types2015 = []
with open('Crimes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2].find('2015') != -1:
            list_of_types2015.append(row[5])
print(Counter(list_of_types2015).most_common(1))


