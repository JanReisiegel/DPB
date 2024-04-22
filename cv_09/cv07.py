from elasticsearch import Elasticsearch
from pprint import pprint

INDEX_NAME = 'person'
ELASTIC_PASSWORD = 'lenovo'

def print_delimiter(n):
    print('\n', '#' * 10, 'Úloha', n, '#' * 10, '\n')


# Připojení k ES
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'https'}], basic_auth=('elastic', ELASTIC_PASSWORD))


# Kontrola zda existuje index 'person'
if not es.indices.exists(index=INDEX_NAME):
    # Vytvoření indexu
    es.indices.create(index=INDEX_NAME)

# Index není potřeba vytvářet - pokud neexistuje, tak se automaticky vytvoří při vložení prvního dokumentu

# 1. Vložte osobu se jménem John
print_delimiter(1)
person = {
    'name': 'John',
    'age': 25,
    'job': 'developer',
    'gender': 'male'
}
res = es.index(index=INDEX_NAME, id=1, document=person)
pprint(res)

# 2. Vypište vytvořenou osobu (pomocí get a parametru id)
print_delimiter(2)
res = es.search(index=INDEX_NAME, query={"match": {'name': 'John'}})
pprint(res)

# 3. Vypište všechny osoby (pomocí search)
print_delimiter(3)
res = es.search(index=INDEX_NAME, query={"match_all": {}})
pprint(res)

# 4. Přejmenujte vytvořenou osobu na 'Jane'
print_delimiter(4)
res = es.update(index=INDEX_NAME, id=1, document={'name': 'Jane'})
pprint(res)

# 5. Smažte vytvořenou osobu
print_delimiter(5)
res = es.delete(index=INDEX_NAME, id=1)
pprint(res)

# 6. Smažte vytvořený index
print_delimiter(6)
res = es.indices.delete(index=INDEX_NAME)
pprint(res)
