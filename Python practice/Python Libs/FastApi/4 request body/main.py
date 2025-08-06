from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uvicorn
from schemas.user import User
app = FastAPI()

@app.get("/")
def Users():
    return JSONResponse(content={"users": "admin", "role": "admin", "email": "admin@gmail.com"}, status_code=status.HTTP_200_OK)

@app.post("/")
def CreateUser(user: User) -> User:
    print(user)
    return JSONResponse(content={"message": "User created"}, status_code=status.HTTP_201_CREATED)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
