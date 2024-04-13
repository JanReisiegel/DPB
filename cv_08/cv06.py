from init import collection
from pprint import pprint

'''
DPB - 6. cvičení - Agregační roura a Map-Reduce

V tomto cvičení si můžete vybrat, zda ho budete řešit v Mongo shellu nebo pomocí PyMongo knihovny.

Před testováním Vašich řešení si nezapomeňte zapnout Mongo v Dockeru - používáme stejná data jako v minulých cvičeních.

Pro pomoc je možné např. použít https://api.mongodb.com/python/current/examples/aggregation.html a přednášku.

Všechny výsledky limitujte na 10 záznamů. Nepoužívejte české názvy proměnných!

Struktura záznamu v db:
{
  "address": {
     "building": "1007",
     "coord": [ -73.856077, 40.848447 ],
     "street": "Morris Park Ave",
     "zipcode": "10462"
  },
  "borough": "Bronx",
  "cuisine": "Bakery",
  "grades": [
     { "date": { "$date": 1393804800000 }, "grade": "A", "score": 2 },
     { "date": { "$date": 1378857600000 }, "grade": "A", "score": 6 },
     { "date": { "$date": 1358985600000 }, "grade": "A", "score": 10 },
     { "date": { "$date": 1322006400000 }, "grade": "A", "score": 9 },
     { "date": { "$date": 1299715200000 }, "grade": "B", "score": 14 }
  ],
  "name": "Morris Park Bake Shop",
  "restaurant_id": "30075445"
}
'''


def print_delimiter(n):
    print('\n', '#' * 10, 'Úloha', n, '#' * 10, '\n')


'''
Agregační roura
Zjistěte počet restaurací pro každé PSČ (zipcode)
 a) seřaďte podle zipcode vzestupně
 b) seřaďte podle počtu restaurací sestupně
Výpis limitujte na 10 záznamů a k provedení použijte collection.aggregate(...)
'''
print_delimiter('1 a)')
cursor = collection.aggregate([
    {'$group': {'_id': '$address.zipcode', 'count': {'$sum': 1}}},
    {'$sort': {'_id': 1}},
    {'$limit': 10}
])
for restaurant in cursor:
    pprint(restaurant)

print_delimiter('1 b)')
cursor = collection.aggregate([
   {'$group': {'_id': '$address.zipcode', 'count': {'$sum': 1}}},
   {'$sort': {'count': -1}},
   {'$limit': 10}
])

for restaurant in cursor:
    pprint(restaurant)


'''
Agregační roura

Restaurace obsahují pole grades, kde jsou jednotlivá hodnocení. Vypište průměrné score pro každou hodnotu grade.
V agregaci vynechte grade pro hodnotu "Not Yet Graded" (místo A, B atd. se může vyskytovat tento řetězec).

'''
print_delimiter(2)
cursor = collection.aggregate([
   {'$unwind': '$grades'},
   {'$match': {'grades.grade': {'$ne': 'Not Yet Graded'}}},
   {'$group': {'_id': '$grades.grade', 'average': {'$avg': '$grades.score'}}},
   {'$limit': 10}
])
for restaurant in cursor:
    pprint(restaurant)

'''
BONUS
'''

'''
Zjistěte 5 restaurací s nejlepším průměrným score pro známku A.
Restaurace s méně než třemi hodnoceními nebudou uvažovány.
Úlohu vyřešte pomocí collection.agregate.
'''
print_delimiter('BONUS 1')
cursor = collection.aggregate([
   {'$group': {'_id': '$restaurant_id', 'average_score': {'$avg': '$grades.score'}, 'count': {'$sum': 1}}},
   {'$match': {'count': {'$gte': 3}, '_id': {'$ne': None}}},
   {'$sort': {'average_score': -1}},
   {'$limit': 5}
])
'''
Nalezněte nejlepší restauraci pro každý typ kuchyně (cuisine).
Rozšiřte předchozí úlohu. Úlohu řešte pomocí collection.agregate.
'''
print_delimiter('BONUS 2')
cursor = collection.aggregate([
   {'$group': {'_id': '$restaurant_id', 'average_score': {'$avg': '$grades.score'}, 'count': {'$sum': 1}}},
   {'$match': {'count': {'$gte': 3}, '_id': {'$ne': None}}},
   {'$sort': {'average_score': -1}}
])


'''
Nalezněte všechny restaurace s víceslovným názvem (name).
Restaurace musí mít alespoň 2 hodnocení vyšší než 10.
Úlohu řešte pomocí collection.agregate.
'''
print_delimiter('BONUS 3')
cursor = collection.aggregate([
   {'$match': {'name': {'$regex': ' '}, 'grades': {'$size': {'$gt': 10}}, 'grades.score': {'$gt': 10}}},
   {'$group': {'_id': '$name', 'count': {'$sum': 1}}},
   {'$limit': 10}
])