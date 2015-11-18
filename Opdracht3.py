import csv
import random
f = open('opdracht3.csv', 'w+',newline='')
fieldnames=['nummer','randomnr']
writer = csv.DictWriter(f,fieldnames=fieldnames,delimiter=';')
writer.writeheader()
for i in range(1,101):
    randgetal = random.randint(1,10001)
    writer.writerow({r'nummer':i,r'randomnr':randgetal})
f.close()

