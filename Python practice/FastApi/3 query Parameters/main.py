from fastapi import FastAPI
from typing import List, Dict
import uvicorn

app = FastAPI()

data:List[Dict[str, int]] = [
    {"id": 1, "name": "Ipad M-10", "price": 100000},
    {"id": 2, "name": "Ipad M-11", "price": 150000},
    {"id": 3, "name": "Ipad M-12", "price": 200000},
    {"id": 4, "name": "Ipad M-13", "price": 250000},
    {"id": 5, "name": "Ipad M-14", "price": 300000},
]

# Get query parameter http://127.0.0.1:8000/?query=admin
@app.get("/")
async def Home(query: str | None = None):
    if query:
        filtered_data = []
        for item in data:
            if query.lower() in item["name"].lower():
                filtered_data.append(item)
        return {"data": filtered_data}
    return {"data": data}

# # Get path parameter http://127.0.0.1:8000/1
# @app.get("/")
# # this is called pagination
# async def Home(skip: int = 0, limit: int = 10):
#     if skip > len(data):
#         return {"data": []}
#     return {"data": data[skip:skip+limit]}

# @app.get("/product/{id}")
# # this is called path parameter
# async def product(id: int):
#     if id > len(data):
#         return {"data": []}
#     return {"data": data[id-1]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
