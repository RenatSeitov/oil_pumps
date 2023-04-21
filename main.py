from fastapi import FastAPI
from api import pumps, users, token

app = FastAPI()


app.include_router(pumps.router)
app.include_router(users.router)
app.include_router(token.router)

@app.get("/")
async def get_hello():
    return {"name": "Hello"}
