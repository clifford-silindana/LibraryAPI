from django.shortcuts import render
from library.models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from django.http import HttpResponse

# Create your views here.

@api_view(["GET", "POST"])
def getBooks(request):
    if request.method == "GET":
        book = Book.objects.all()
        serialized_data = BookSerializer(book, many = True)
        return Response(serialized_data.data)
    else:
        data = request.data
        serialized_data = BookSerializer(data = data)

        if serialized_data.is_valid():
            serialized_data.save()
        return Response(serialized_data.data)


@api_view(["GET", "PUT", "DELETE"])
def getBook(request, id):
    if request.method == "GET":
        book = Book.objects.get(id = id)
        serialized_data = BookSerializer(book, many = False)

        return Response(serialized_data.data)
    elif request.method == "PUT":
        book = Book.objects.get(id = id)
        data = request.data
        serialized_data = BookSerializer(instance = book, data= data)

        if serialized_data.is_valid():
            serialized_data.save()
        return Response(serialized_data.data)

    else:

        book = Book.objects.get(id = id)
        book.delete()
        return HttpResponse("Book deleted")



"""@api_view(["POST"])
def createBook(request):
    data = request.data
    serialized_data = BookSerializer(data = data)

    if serialized_data.is_valid():
        serialized_data.save()
    return Response(serialized_data.data)

@api_view(["PUT"])
def updateBook(request, id):
    book = Book.objects.get(id = id)
    data = request.data
    serialized_data = BookSerializer(instance = book, data= data)

    if serialized_data.is_valid():
        serialized_data.save()
    return Response(serialized_data.data)

@api_view(["DELETE"])
def deleteBook(request, id):
    book = Book.objects.get(id = id)
    book.delete()
    return HttpResponse("Book deleted")
"""
#getBooks
#getBook

#api/users
#API/USERS/ID


#RESTFUL ENDPOINTS
#books GET, 
#books POST
#books/id PUT
#books/id GET
#books/id delete








