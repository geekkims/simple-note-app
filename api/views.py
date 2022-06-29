from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note
from api import serializers

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes=[
        {
            'Endpoint':'/notes',
            'method':'GET',
            'body':None,
            'decription':'Returns an array of notes'
        },
          {
            'Endpoint':'/notes/id',
            'method':'GET',
            'body':None,
            'decription':'Returns a single note object'
        },

          {
            'Endpoint':'/notes/create/',
            'method':'POST',
            'body':{'body':""},
            'decription':'Craetes an existing note with data sent in'
        },

           {
            'Endpoint':'/notes/id/update/',
            'method':'PUT',
            'body':{'body':""},
            'decription':'Craetes an existing note with data sent in'
        },

            {
            'Endpoint':'/notes/id/delete',
            'method':'DELETE',
            "body": None,
            'decription':'Delete an existing note with data sent in'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer= NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer= NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data
    note= Note.objects.create(
        body=data['body']
    )
    serializers = NoteSerializer(note, many=False)
    return Response(serializers.data)



@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note=Note.objects.get(id=pk)
    serializers = NoteSerializer(note, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)
    

@api_view(['DELETE'])
def deleteNote(request,pk):
    note=Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')


