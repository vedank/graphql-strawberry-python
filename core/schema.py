import strawberry
from typing import List
from strawberry.django.views import AsyncGraphQLView
from core.types import BookInput, BookType
from core.models import Book

@strawberry.type
class Query:
    @strawberry.field
    def all_books(self) -> List[BookType]:
        return Book.objects.all()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_book (self, input: BookInput) -> BookType:
        book = Book.objects.create(
            title= input.title,
            author = input.author,
            published_year = input.published_year
        )
        return book
    
    @strawberry.mutation
    def update_book(self, input:BookInput) -> BookType:
        book = Book.objects.get(id = input.id)
        for field, value in input.__dict__.items():
            setattr(book, field, value)
        book.save()
        return book
    
    @strawberry.mutation
    def delete_book(self, id: int) -> bool:
        try:
            book = Book.objects.get(id=id)
            book.delete()
            return True
        except Book.DoesNotExist:
            return False
    
schema = strawberry.Schema(query=Query, mutation=Mutation)