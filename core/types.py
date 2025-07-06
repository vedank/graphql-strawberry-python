import strawberry
from strawberry import auto, input
from strawberry_django import type
from core.models import Book

@type(model=Book)
class BookType:
    id: auto
    title: auto
    author: auto
    published_year: auto

@input
class BookInput:
    title: str
    author : str
    published_year : int

