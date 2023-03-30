import json
import os
import random

from src.Agent import Agent
from src.Entities import GarbageTruck, GarbageDump, House, Tree, AsphaltRoad, GravelRoad
from src.Environment import Environment
from src.Game import Game
from src.Garbage import Garbage


class Project:
    def __init__(self, name, fieldWidth, fieldHeight):
        self.garbage = Garbage()
        self.environmentMap = None
        self.wasteDatabase = None
        self.name = name
        self.fieldWidth = fieldWidth
        self.fieldHeight = fieldHeight
        self.environmentMap = self.loadEnvironmentMap()
        self.wasteDatabase = self.loadWasteDatabase()
        self.environment = self.setEnvironment()
        self.agent = Agent(self.environment, self.environment.garbageTruck)
        self.solution = None
        self.game = self.setGame()

    def loadWasteDatabase(self):
        path = ["..", "resources", "json", "wasteDatabase.json"]
        file = open(os.path.join(*path))
        return json.load(file)

    def printWasteDatabase(self):
        if self.wasteDatabase is not None:
            for x in self.wasteDatabase["wasteTypes"].keys():
                print(x)

    def loadEnvironmentMap(self):
        path = ["..", "resources", "json", "environmentMap.json"]
        file = open(os.path.join(*path))
        return json.load(file)

    def setEnvironment(self):
        x = random.randint(1, 6)
        rows = self.environmentMap[f"{x}"]["rows"]
        columns = self.environmentMap[f"{x}"]["columns"]
        garbageTruck = GarbageTruck(0, 0, 0)
        garbageDump = GarbageDump(0, 0)
        houses = []
        trees = []
        asphaltRoads = []
        gravelRoads = []
        for i in range(rows):
            for j in range(columns):
                entity = self.environmentMap[f"{x}"]["map"][i][j]
                if entity == 1:
                    garbageTruck.setPos(j, i)
                elif entity == 2:
                    garbageDump.setPos(j, i)
                elif entity == 3:
                    houses.append(House(j, i, self.garbage.getRandomWaste()))
                elif entity == 4:
                    trees.append(Tree(j, i))
                elif entity == 5:
                    asphaltRoads.append(AsphaltRoad(j, i))
                elif entity == 6:
                    gravelRoads.append(GravelRoad(j, i))
        return Environment(rows, columns, garbageTruck, garbageDump, houses, trees, asphaltRoads, gravelRoads)

    def setGame(self):
        return Game(self.name, self.environment.rows, self.environment.columns, self.fieldWidth,
                    self.fieldHeight)
