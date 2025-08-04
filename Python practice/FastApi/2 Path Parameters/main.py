from fastapi import FastAPI
from enum import Enum
import uvicorn

app = FastAPI()

class UserType(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

@app.get("/userValidation/")
async def userValidation(user_type: UserType):
    # FastAPI self validation but you want to validate
    # return {
    #     "status": "200",
    #     "user_type": user_type.value
    # }
    # first check user_type is in UserType
    #if user_type == UserType.ADMIN or user_type == UserType.USER or user_type == UserType.GUEST:
    
    # if user_type not in UserType:
    #     return {
    #         "status": "400",
    #         "user_type": "Invalid user type"
    #     }
    # return {
    #     "status": "200",
    #     "user_type": user_type.value
    # }
    
    if user_type == UserType.ADMIN:
        return {
            "status": "200",
            "user_type": user_type.value
        }
    if user_type == UserType.USER:
        return {
            "status": "200",
            "user_type": user_type.value
        }
    if user_type == UserType.GUEST:
        return {
            "status": "200",
            "user_type": user_type.value
        }
    return {
        "status": "400",
        "user_type": "Invalid user type"
    }
    

@app.get("/users")
async def users():
    return {
        "users": [
            {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "user_type": UserType.ADMIN.value},
            {"id": 2, "name": "Butler", "email": "butler@example.com", "user_type": UserType.USER.value},
            {"id": 3, "name": "Steve", "email": "steve@example.com", "user_type": UserType.GUEST.value},
        ]
    }

@app.get("/user_profile/{id}") # this is called path parameter
async def profile(id: int): # this is called path parameter and type hinting is int
    users = [
        {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "user_type": UserType.ADMIN.value},
        {"id": 2, "name": "Butler", "email": "butler@example.com", "user_type": UserType.USER.value},
        {"id": 3, "name": "Steve", "email": "steve@example.com", "user_type": UserType.GUEST.value},
    ]

    for user in users:
        if user["id"] == id:
            return {
                "status": "200",
                "profile": user
            }

    return {
        "status": "404",
        "message": "User not found"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
