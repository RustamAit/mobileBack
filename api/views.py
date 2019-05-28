from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
# Create your views here.
from api.models import *
from api.serializers import *
from api.gameLogic import gameGenerator


class PersonListView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class GameSessionView(viewsets.ModelViewSet):
    queryset = GameSession.objects.all()
    serializer_class = GameSessionSerializer

@api_view(["GET"])
def createPerson(request):
    phoneNumber = request.GET["phoneNumber"]
    if phoneNumber:
        person = Person()
        person.phoneNumber = phoneNumber
        person.fCMToken = "asdasdasd"
        person.save()
        return Response({"id": person.id, "phoneNumber": person.phoneNumber, "fCMToken": person.fCMToken},status.HTTP_200_OK)
    else:
        return Response({"success": False}, status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def createGame(request):
    playerId = request.GET['playerId']
    totalNumberOfPlayers = request.GET['totalNumberOfPlayers']
    game = gameGenerator.generate_game(int(totalNumberOfPlayers))
    if game is not None:
        players = [Person.objects.get(id= playerId)]
        gameSession = GameSession()
        gameSession.location = game.location
        gameSession.spyNumber = game.spyNumber
        gameSession.totalNumberOfPlayers = game.totalNumberOfPlayers
        gameSession.currentPlayerNumber = 1
        gameSession.readyPlayerNumber = 1
        gameSession.finishedPlayerNumber = 0
        gameSession.save()
        gameSession.players.set(players)
        gameSession.save()
        if gameSession.spyNumber == gameSession.currentPlayerNumber:
            return Response({"location": "Spy"}, status=status.HTTP_200_OK)
        else:
            return Response({"location": gameSession.location, "gameId": gameSession.id}, status=status.HTTP_200_OK)

    else:
        return Response({"error": "invalid number of players"}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def joinGame(request):
    playerId = request.GET['playerId']
    gameSessionId = request.GET['gameId']
    person = Person.objects.get(id = playerId)
    gameSession = GameSession.objects.get(id = gameSessionId)
    if gameSession.totalNumberOfPlayers != gameSession.currentPlayerNumber:
        gameSession.players.add(person)
        gameSession.readyPlayerNumber += 1
        gameSession.currentPlayerNumber += 1
        gameSession.save()
        if gameSession.totalNumberOfPlayers == gameSession.currentPlayerNumber:
            print("UHAHAHAHAHA")

        if gameSession.spyNumber == gameSession.currentPlayerNumber-1:
            return Response({"location": "Spy"}, status=status.HTTP_200_OK)
        else:
            return Response({"location": gameSession.location}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "game already started"}, status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["GET"])
def finishGame(request):
    gameSessionId = request.GET['gameId']
    gameSession = GameSession.objects.get(id = gameSessionId)
    gameSession.finishedPlayerNumber += 1
    gameSession.save()
    if gameSession.finishedPlayerNumber == gameSession.totalNumberOfPlayers:
        print("hehehehehe")

    return Response({"success": True}, status.HTTP_200_OK)


@api_view(["GET"])
def leaveGame(request):
    playerId = request.GET['playerId']
    gameSessionId = request.GET['gameId']
    person = Person.objects.get(id = playerId)
    gameSession = GameSession.objects.get(id = gameSessionId)
    gameSession.players.remove(person)
    gameSession.readyPlayerNumber -= 1
    gameSession.currentPlayerNumber -= 1
    gameSession.save()
    return Response({"success": True}, status.HTTP_200_OK)
