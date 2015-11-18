##We gaan nu alles met elkaar combineren:
####a. Lees het werkboek uit de eerste opdracht regel voor regel in.
####b. Schrijf tegelijkertijd een tweede werkboek met dezelfde informatie per klant, maar nu aangevuld met extra kolommen, namelijk:
######i. Een kolom met â€œLeeftijdâ€ (bereken aan de hand van de geboortedatum de leeftijd).
######ii. Een kolom met â€œPasswordâ€ (genereer een willekeurig wachtwoord van 8 karakters met de random module).
######iii. Een kolom met â€œKlantnummerâ€ (een oplopend getal).
######iv. Een kolom met â€œUsernameâ€ (genereer de username als â€œNaamâ€+â€Geboortejaarâ€.

#importeer functies
import csv
import random
import string
import datetime
#open het eerste bestand waaruit gelezen wordt.
f = open('opdracht2.csv', 'rt')
reader = csv.reader(f, delimiter=';') #scheidingsteken waarop gezocht wordt is een ;
#skip de header van de gelezen file
next(reader, None)
#open het bestand waarin geschreven gaa worden
g = open('opdracht5.csv', 'w+',newline='\n')
#bepaald de headers (eerste regel)
fieldname=['Voornaam','Achternaam','Geboortejaar','E-mail','Telefoonnummer','Leeftijd', 'Password','Klantnummer','Username']
#bepaald dat g als fieldnames (header) de hierboven aangegeven headers gebruikt en alles scheidt met een ;
writer = csv.DictWriter(g,fieldnames=fieldname,delimiter=';')
#schrijft daadwerkelijk eerst de header.
writer.writeheader()
#om het huidige jaar te bepalen (voor de leeftijd)
now = datetime.datetime.now()
year = now.year
#om een line te maken van tekst met alle letters en cijfers
text = string.ascii_letters + string.digits
#het eerste klantnummer
klantnummer = 10001
#gaat elke rij af in het bestand dat gelezen wordt, alleen niet de header.
for row in reader:
    leeftijd = year - int(row[2]) #bepaalt leeftijd door het geboortejaar te lezen en deze van het huidige jaar af te trekken.
    password = ''.join(random.choice(text) for _ in range(8)) #bepaald het password door random 8 getallen uit de net gedefinieerde line van letters en cijfers te pakken.
    username = row[0]+row[2] #plakt naam en geboortejaar aan elkaar voor de gebruikersnaam.
    #schrijft alles weg per rij.
    writer.writerow({'Voornaam':row[0],'Achternaam':row[1],'Geboortejaar':row[2],'E-mail':row[3],'Telefoonnummer':row[4],'Leeftijd':leeftijd,'Password':password,'Klantnummer':klantnummer,'Username':username})
    #telt 1 bij het klantnummer op zodat deze oploopt.
    klantnummer += 1
#sluit de files weer.
f.close()
g.close()