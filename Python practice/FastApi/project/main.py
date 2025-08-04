from fastapi import FastAPI
from api import api

app = FastAPI()

# Include Routers
app.include_router(api.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
