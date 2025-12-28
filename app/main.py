from fastapi import FastAPI

import uvicorn

from app.api.routers import auth, users


app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
def hello_world():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
