# 3D Dictionary
# products = {
#     "category": {
#         "electronics": [
#             {
#                 "id": 1,
#                 "title": "Ipad M-10",
#                 "price": 100000,
#                 "status": 200
#             },
#             {
#                 "id": 2,
#                 "title": "Samsung Galaxy Tab",
#                 "price": 85000,
#                 "status": 200
#             }
#         ],
#         "furniture": [
#             {
#                 "id": 3,
#                 "title": "Wooden Chair",
#                 "price": 5000,
#                 "status": 200
#             },
#             {
#                 "id": 4,
#                 "title": "Study Table",
#                 "price": 8000,
#                 "status": 200
#             }
#         ]
#     }
# }
# print(products)
# print(products['products'])
# print(products['products']['electronics'])
# print(products['products']['electronics'][0])
# print(products['products']['electronics'][0]['title'])
# print(products['products']['electronics'][0]['price'])
# print(products['products']['electronics'][0]['status'])
# print(type(products))
# print(type(products['products']))
# print(type(products['products']['electronics']))
# print(type(products['products']['electronics'][1]))
# print(type(products['products']['electronics'][1]['price']))
# print(type(products['products']['electronics'][1]['status']))

products = {
    "product": [
        {
            "id": 1,
            "status": 200,
            "title": "Ipad M-10",
            "price": 100000,
            "description": "Ipad M-10 is a great product"
        },
        {
            "id": 2,
            "status": 200,
            "title": "Ipad M-11",
            "price": 200000,
            "description": "Ipad M-11 is a great product"
        },
        {
            "id": 3,
            "status": 200,
            "title": "Ipad M-12",
            "price": 300000,
            "description": "Ipad M-12 is a great product"
        }
    ]
}
print(products)
print(products['product'])
print(products['product'][1])
print(products['product'][1]['title'])
print(products['product'][1]['price'])
print(products['product'][1]['description'])
print(products['product'][1]['status'])
print(type(products))
print(type(products['product']))
print(type(products['product'][0]))
print(type(products['product'][0]['price']))
print(type(products['product'][0]['description']))
print(type(products['product'][0]['status']))
