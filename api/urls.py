from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.getBooks, name = "get books"),
    path("books/<int:id>/", views.getBook, name = "get book"),
]
