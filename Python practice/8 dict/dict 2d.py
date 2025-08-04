# 2D Dictionary

# products = {
#     1: {
#         "id": 1,
#         "title": "Ipad M-10",
#         "price": 100000,
#         "description": "Ipad M-10 is a great product",
#         "status": 200
#     },
#     2: {
#         "id": 2,
#         "title": "Ipad M-11",
#         "price": 200000,
#         "description": "Ipad M-11 is a great product",
#         "status": 200
#     },
#     3: {
#         "id": 3,
#         "title": "Ipad M-12",
#         "price": 300000,
#         "description": "Ipad M-12 is a great product",
#         "status": 200
#     }
# }
# print(products)
# print(products[1])
# print(products[1]['title'])
# print(products[1]['price'])
# print(products[1]['description'])
# print(products[1]['status'])


# print(type(products))
# print(type(products[1]))
# print(type(products[1]['title']))
# print(type(products[1]['price']))
# print(type(products[1]['description']))
# print(type(products[1]['status']))


# products = [
#     {
#         "id": 1,
#         "title": "Ipad M-10",
#         "price": 100000,
#         "description": "Ipad M-10 is a great product",
#         "status": 200
#     },
#     {
#         "id": 2,
#         "title": "Ipad M-11",
#         "price": 200000,
#         "description": "Ipad M-11 is a great product",
#         "status": 200
#     },
#     {
#         "id": 3,
#         "title": "Ipad M-12",
#         "price": 300000,
#         "description": "Ipad M-12 is a great product",
#         "status": 200
#     }
# ]
# print(products)
# print(products[1])
# print(products[1]['title'])
# print(products[1]['price'])
# print(products[1]['description'])
# print(products[1]['status'])
# print(type(products))
# print(type(products[1]))
# print(type(products[1]['price']))
# print(type(products[1]['description']))
# print(type(products[1]['status']))

products = {
    "product": [
        {
            "id": 1,
            "status": 200,
            "title": "Ipad M-10",
            "price": 100000,
            "description": "Ipad M-10 is a great product"
        }
    ]
}
print(products)
print(products['product'])
print(products['product'][0])
print(products['product'][0]['title'])
print(products['product'][0]['price'])
print(products['product'][0]['description'])
print(products['product'][0]['status'])
print(type(products))
print(type(products['product']))
print(type(products['product'][0]))
print(type(products['product'][0]['price']))
print(type(products['product'][0]['description']))
print(type(products['product'][0]['status']))