from typing import List, Dict

# products: List[Dict[str, int]] = [
#     {"id": 1, "price": 100},
#     {"id": 2, "price": 150},
# ]

# print(products)
# print(products[1])
# print(products[1]['price'])
# print(type(products))
# print(type(products[1]))
# print(type(products[1]['price']))


db:Dict[str, List[Dict[str, int, float]]] = {
    "products": [
        {
            "id": 1,
            "price": 100.0,
            "title": "Ipad M-10",
            "description": "Ipad M-10 is a great product",
            "status": 200
        },
        {
            "id": 2,
            "price": 150.0,
            "title": "Ipad M-11",
            "description": "Ipad M-11 is a great product",
            "status": 200
        }
    ]
}
print(db)
print(db['products'])
print(db['products'][1])
print(db['products'][1]['title'])
print(db['products'][1]['price'])
print(db['products'][1]['description'])
print(db['products'][1]['status'])
print(type(db))
print(type(db['products']))
print(type(db['products'][0]))
print(type(db['products'][0]['price']))
print(type(db['products'][0]['description']))
print(type(db['products'][0]['status']))

