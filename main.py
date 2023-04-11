from fastapi import FastAPI
from api import pumps

app = FastAPI()


app.include_router(pumps.router)

@app.get("/")
async def get_hello():
    return {"name": "Hello"}
