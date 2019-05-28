import random


class LocationGenerator:

    @staticmethod
    def getLocations():
        locations = ["Школа", "Госпиталь", "Сад", "Кинотеатр", "Тюрьма", "Стадион", "Университет",
                     "Полицейский участок", "Тюрма"]
        return locations


class Game:
    location = ""
    totalNumberOfPlayers = 0
    spyNumber = 0

    def __init__(self,location, totalNumberOfPlayers, spyNumber):
        self.location = location
        self.totalNumberOfPlayers = totalNumberOfPlayers
        self.spyNumber = spyNumber


def generate_game(totalNumberOfPlayers):
    if totalNumberOfPlayers<3:
        return None
    else:
        spyNumber = random.randint(1, totalNumberOfPlayers)
        locations = LocationGenerator.getLocations()
        location = locations[random.randint(0, len(locations)-1)]
        return Game(totalNumberOfPlayers = totalNumberOfPlayers, location = location, spyNumber = spyNumber)
