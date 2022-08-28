import strawberry
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Book:
    title: str
    author: str


def get_books() -> list[Book]:
    return [
        Book(
            title="A psicologia financeira",
            author="Morgan Housel"
        )
    ]


@strawberry.type
class Query:
    books: list[Book] = strawberry.field(resolver=get_books)


schema = strawberry.Schema(query=Query)
book_graphql = GraphQLRouter(schema=schema)
