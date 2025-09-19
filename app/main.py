from fastapi import FastAPI
from app import models, database
from app.routers import users

# Cria as tabelas no banco
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Inclui o router de usuários
app.include_router(users.router)
