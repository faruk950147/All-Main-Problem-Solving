# fast api two types function supported 
#1. Function based API
# ************** normal function **************

# from fastapi import FastAPI
# import uvicorn
# app = FastAPI()

# @app.get("/")
# def Home():
#     return {
#         "Status": 200,
#         "Message": "Hello World"
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

# 2 ************** async function **************

# from fastapi import FastAPI
# import uvicorn
# app = FastAPI()

# @app.get("/")
# async def Home():
#     return {
#         "Status": 200,
#         "Message": "Hello World"
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)




# 3 ************** when the use async or normal function **************

# ***************** when the just return data simple work then use normal function

# ***************** when the external work (Database, Network, API call) then use async function

