import csv

c = csv.reader(open('nasdaq.csv'))

rows = []
for row in c:
    rows.append(row)
print(range(len((rows))))
