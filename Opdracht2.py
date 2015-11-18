import csv

f = open('opdracht2.csv', 'rt')
reader = csv.reader(f, delimiter=';')
for row in reader:
    print (row[0], row[3])
f.close()
