import csv

c = csv.reader(open('nasdaq.csv'))

rows = []
for row in c:
    rows.append(row)
listToStr = ' '.join([str(elem) for elem in rows])
print(listToStr[0])
