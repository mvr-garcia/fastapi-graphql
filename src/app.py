from fastapi import FastAPI
from src.schema import book_graphql


app = FastAPI()

app.include_router(book_graphql, prefix="/graphql")
