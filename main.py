from fastapi import FastAPI
from routes.user import user

app= FastAPI(
    title= " Mi primera  REST CON FastAPI y MONGODB",
    description= "un simple REST con FastApi y MONGODB para practicar"
)

app.include_router(user)
