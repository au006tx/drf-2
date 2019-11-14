from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework import status
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello')

@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def api_author_view(request):

    if request.method == 'GET':
        try:
            author = Author.objects.get()
        except Author.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    if request.method == 'GET' and pk is None:
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    

