from fastapi import FastAPI
from database.db import Base, engine
from routers import user

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router, tags=["User"])

@app.get("/", tags=["Main"])
def main():
    return {"message": "Hello World"}