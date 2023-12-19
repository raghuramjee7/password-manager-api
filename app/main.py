from fastapi import FastAPI
from database import model, connect
from fastapi.middleware.cors import CORSMiddleware
from routers import user, item, auth

app = FastAPI()

# CORS
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://credapi.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # allow all http methods
    allow_headers=["*"], # allow all http headers
)

model.Base.metadata.create_all(bind = connect.engine) 

@app.get("/")
async def main():
    return {"message": "Welcome to the Password Manager API"}

app.include_router(user.router)
app.include_router(item.router)
app.include_router(auth.router)
