from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uvicorn
app = FastAPI()

# @app.get("/")
# async def Home():
#     return {
#         "id": 1,
#         "status": 200,
#         "title": "Ipad M-10",
#         "price": 100000,
#         "description": "Ipad M-10 is a great product"
#     }

# @app.get("/")
# async def Home():
#     return {
#         "product": { #just for one product
#             "id": 1,
#             "status": 200,
#             "title": "Ipad M-10",
#             "price": 100000,
#             "description": "Ipad M-10 is a great product"
#         }
#     }


@app.get("/")
async def Home():
    return JSONResponse(content={
        "products": [
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
                "price": 100000,
                "description": "Ipad M-11 is a great product"
            },
            {
                "id": 3,
                "status": 200,
                "title": "Ipad M-12",
                "price": 100000,
                "description": "Ipad M-12 is a great product"
            },
        ]
    }, status_code=status.HTTP_200_OK)
  

@app.get("/product/{id}") # this is called path parameter
async def product(id: int): # this is called path parameter and type hinting is int
    return JSONResponse(content={
        "product": {
            "id": id,
            "status": 200,
            "title": "Ipad M-10",
            "price": 100000,
            "description": "Ipad M-10 is a great product"
        }
    }, status_code=status.HTTP_200_OK)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

