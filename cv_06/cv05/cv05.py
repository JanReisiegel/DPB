from pprint import pprint
from init import collection
import datetime

print(collection.find_one())

'''
DPB - 5. Cvičení
Implementujte jednotlivé body pomocí PyMongo knihovny - rozhraní
je téměř stejné jako v Mongo shellu.
Před testováním Vašich řešení si nezapomeňte zapnout Mongo v Dockeru.
Pro pomoc je možné např.
použít https://www.w3schools.com/python/python_mongodb_getstarted.asp
Funkce find vrací kurzor - pro vypsání výsledku
je potřeba pomocí foru iterovat nad kurzorem:
cursor = collection.find(...)
for restaurant in cursor:
    print(restaurant) # případně print(restaurant['name'])
Všechny výsledky limitujte na 10 záznamů. Nepoužívejte české názvy proměnných!
'''


def print_delimiter(n):
    print('\n', '#' * 10, 'Úloha', n, '#' * 10, '\n')


# 1. Vypsání všech restaurací
print_delimiter(1)

cursor = collection.find().limit(10)
for restaurant in cursor:
    pprint(restaurant)

# 2. Vypsání všech restaurací - pouze názvů, abecedně seřazených
print_delimiter(2)

cursor = collection.find({}, {'name': 1, '_id': 0}).sort('name', 1).limit(10)
for restaurant in cursor:
    pprint(restaurant)

# 3. Vypsání pouze 5 záznamů z předchozího dotazu
print_delimiter(3)

cursor = collection.find({}, {'name': 1, '_id': 0}).sort('name', 1).limit(5)
for restaurant in cursor:
    pprint(restaurant)

# 4. Zobrazte dalších 10 záznamů
print_delimiter(4)

cursor = collection.find({}, {'name': 1, '_id': 0}).sort('name', 1).skip(10).limit(10)
for restaurant in cursor:
    pprint(restaurant)

# 5. #Vypsání restaurací ve čtvrti Bronx (čtvrť = borough)
print_delimiter(5)

cursor = collection.find({'borough': 'Bronx'}).limit(10)
for restaurant in cursor:
    pprint(restaurant)

# 6. Vypsání restaurací, jejichž název začíná na písmeno M
print_delimiter(6)

cursor = collection.find({'name': {'$regex': '^M'}}).limit(10)
for restaurant in cursor:
    pprint(restaurant)

# 7. Vypsání restaurací, které mají skóre větší než 80
print_delimiter(7)
cursor = collection.find({'grades.score': {'$gt': 80}}).limit(10)
for restaurant in cursor:
    pprint(restaurant)

# 8. Vypsání restaurací, které mají skóre mezi 80 a 90
print_delimiter(8)
cursor = collection.find({'grades.score': {'$gte': 80, '$lte': 90}}).limit(10)
for restaurant in cursor:
    pprint(restaurant)

'''
Bonusové úlohy:
'''

# 9. Vypsání všech restaurací, které mají skóre mezi 80 a 90 a
# zároveň nevaří americkou (American) kuchyni
print_delimiter(9)
cursor = collection.find({'grades.score': {'$gte': 80, '$lte': 90}, 'cuisine': {'$ne': 'American'}}).limit(10)
for restaurant in cursor:
    pprint(restaurant)

# 10. Vypsání všech restaurací, které mají alespoň osm hodnocení
print_delimiter(10)

cursor = collection.find({'grades.7': {'$exists': True}}).limit(10)
for restaurant in cursor:
    pprint(restaurant)

# 11. Vypsání všech restaurací, které mají alespoň jedno hodnocení z roku 2014 
print_delimiter(11)

cursor = collection.find({'grades.date': {'$gte': datetime.datetime(2014, 1, 1), '$lte': datetime.datetime(2014, 12, 31)}}).limit(10)
for restaurant in cursor:
    pprint(restaurant)

'''
V této části budete opět vytvářet vlastní restauraci.

Řešení:
Vytvořte si vaši restauraci pomocí slovníku a poté ji vložte do DB.
restaurant = {
    ...
}
'''

restaurant = {
    "address": {
        "building": "900",
        "coord": [50.7669883, 15.0523119],
        "street": "Hrazená",
        "zipcode": "10462"
    },
    "borough": "Rybníček",
    "cuisine": "Czech",
    "name": "Plaudit Liberec",
}

# 12. Uložte novou restauraci (stačí vyplnit název a adresu)
print_delimiter(12)

cursor = collection.insert_one(restaurant)

# 13. Vypište svoji restauraci
print_delimiter(13)

cursor = collection.find({'name': 'Plaudit Liberec'}).limit(1)
for restaurant in cursor:
    pprint(restaurant)

# 14. Aktualizujte svoji restauraci - změňte libovolně název
print_delimiter(14)

cursor = collection.update_one({'name': 'Plaudit Liberec'}, {'$set': {'name': 'PUOR Liberec'}})

# 15. Smažte svoji restauraci
# 15.1 pomocí id (delete_one)
# 15.2 pomocí prvního nebo druhého názvu (delete_many, využití or)
print_delimiter(15)


'''
Poslední částí tohoto cvičení je vytvoření jednoduchého indexu.

Použijte např. 3. úlohu s vyhledáváním čtvrtě Bronx. 
První použijte Váš již vytvořený dotaz a na výsledek použijte:

cursor.explain()['executionStats'] - výsledek si vypište na výstup
a všimněte si položky 'totalDocsExamined'

Poté vytvořte index na 'borough', zopakujte dotaz a porovnejte 
hodnoty 'totalDocsExamined'.

S řešením pomůže 
https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.create_index
'''
print_delimiter(11)
