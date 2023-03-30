import os
import pygame
import pygame_menu
import json

from src.Garbage import Garbage


class Game:
    def __init__(self, name, rows, columns, fieldWidth, fieldHeight):
        self.garbageTruckImage = None
        self.garbageDumpImage = None
        self.garbageContainerImage = None
        self.obstacleImage = None
        self.emptyImage = None
        self.window = None
        self.fieldWidth = fieldWidth
        self.fieldHeight = fieldHeight
        self.windowName = name
        self.windowHeight = rows * self.fieldHeight
        self.windowWidth = columns * self.fieldWidth

    def loadImages(self):
        self.emptyImage = pygame.transform.scale(
            pygame.image.load(os.path.join("..", "resources", "board", "empty.png")),
            (self.fieldWidth, self.fieldHeight))
        self.grassImage = pygame.transform.scale(
            pygame.image.load(os.path.join("..", "resources", "board", "grass.png")),
            (self.fieldWidth, self.fieldHeight))
        self.garbageTruckImage = pygame.transform.scale(
            pygame.image.load(os.path.join("..", "resources", "board", "truckLeft.png")),
            (self.fieldWidth, self.fieldHeight))
        self.garbageDumpImage = pygame.transform.scale(
            pygame.image.load(os.path.join("..", "resources", "board", "dump.png")),
            (self.fieldWidth, self.fieldHeight))
        self.houseImage1 = pygame.transform.scale(
            pygame.image.load(os.path.join("..", "resources", "board", "house1.png")),
            (self.fieldWidth, self.fieldHeight))
        self.houseImage2 = pygame.transform.scale(
            pygame.image.load(os.path.join("..", "resources", "board", "house2.png")),
            (self.fieldWidth, self.fieldHeight))
        self.houseImage3 = pygame.transform.scale(
            pygame.image.load(os.path.join("..", "resources", "board", "house3.png")),
            (self.fieldWidth, self.fieldHeight))
        self.houseImage4 = pygame.transform.scale(
            pygame.image.load(os.path.join("..", "resources", "board", "house4.png")),
            (self.fieldWidth, self.fieldHeight))
        self.treeImage = pygame.transform.scale(
            pygame.image.load(os.path.join("..", "resources", "board", "tree.png")),
            (self.fieldWidth, self.fieldHeight))
        self.grassImage = pygame.transform.scale(
            pygame.image.load(os.path.join("..", "resources", "board", "grass.png")),
            (self.fieldWidth, self.fieldHeight))
        self.asphaltRoadImage = pygame.transform.scale(
            pygame.image.load(os.path.join("..", "resources", "board", "asphalt.png")),
            (self.fieldWidth, self.fieldHeight))
        self.gravelRoadImage = pygame.transform.scale(
            pygame.image.load(os.path.join("..", "resources", "board", "dirt.png")),
            (self.fieldWidth, self.fieldHeight))

    def startGame(self):
        self.isRunning = True
        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption(self.windowName)

    def endGame(self):
        pygame.quit()

    def menu(self):
        pygame.init()
        def disable():
            menu.disable()
            self.selectedSeason = menu.get_widget('season_selector').get_value()[0][0]
            self.selectedDay = menu.get_widget('day_selector').get_value()[0][0]
            self.startGame()

        def setSeason(selectedValue, seasonNo):
            valueTuple, index = selectedValue
            print("Changed season to: ", valueTuple[0])
            path = ["..", "resources", "json", "wasteDatabase.json"]
            if valueTuple[0] == "Spring":
                file = open(os.path.join(*path))
                loadedFile = json.load(file)
                for x in loadedFile["wastePriorities"].keys():
                    if x == "Spring":
                        priorityTuples = tuple(loadedFile["wastePriorities"]["Spring"].items())
                        return priorityTuples
            elif valueTuple[0] == "Summer":
                file = open(os.path.join(*path))
                loadedFile = json.load(file)
                for x in loadedFile["wastePriorities"].keys():
                    if x == "Spring":
                        priorityTuples = tuple(loadedFile["wastePriorities"]["Summer"].items())
                        return priorityTuples
            elif valueTuple[0] == "Fall":
                file = open(os.path.join(*path))
                loadedFile = json.load(file)
                for x in loadedFile["wastePriorities"].keys():
                    if x == "Spring":
                        priorityTuples = tuple(loadedFile["wastePriorities"]["Fall"].items())
                        return priorityTuples
            else:
                file = open(os.path.join(*path))
                loadedFile = json.load(file)
                for x in loadedFile["wastePriorities"].keys():
                    if x == "Spring":
                        priorityTuples = tuple(loadedFile["wastePriorities"]["Winter"].items())
                        return priorityTuples

        def setDay(selectedValue, dayNo):
            valueTuple, index = selectedValue
            print("Changed season to: ", valueTuple[0])
            path = ["..", "resources", "json", "wasteDatabase.json"]
            if valueTuple[0] == "Monday":
                file = open(os.path.join(*path))
                loadedFile = json.load(file)
                for x in loadedFile["wasteCollection"].keys():
                    if x == "Monday":
                        collectionTuples = tuple(loadedFile["wasteCollection"]["Monday"].items())
                        return collectionTuples
            elif valueTuple[0] == "Tuesday":
                file = open(os.path.join(*path))
                loadedFile = json.load(file)
                for x in loadedFile["wasteCollection"].keys():
                    if x == "Tuesday":
                        collectionTuples = tuple(loadedFile["wasteCollection"]["Tuesday"].items())
                        return collectionTuples
            elif valueTuple[0] == "Wednesday":
                file = open(os.path.join(*path))
                loadedFile = json.load(file)
                for x in loadedFile["wasteCollection"].keys():
                    if x == "Wednesday":
                        collectionTuples = tuple(loadedFile["wasteCollection"]["Wednesday"].items())
                        return collectionTuples
            elif valueTuple[0] == "Thursday":
                file = open(os.path.join(*path))
                loadedFile = json.load(file)
                for x in loadedFile["wasteCollection"].keys():
                    if x == "Thursday":
                        collectionTuples = tuple(loadedFile["wasteCollection"]["Thursday"].items())
                        return collectionTuples
            elif valueTuple[0] == "Friday":
                file = open(os.path.join(*path))
                loadedFile = json.load(file)
                for x in loadedFile["wasteCollection"].keys():
                    if x == "Friday":
                        collectionTuples = tuple(loadedFile["wasteCollection"]["Friday"].items())
                        return collectionTuples
            elif valueTuple[0] == "Saturday":
                file = open(os.path.join(*path))
                loadedFile = json.load(file)
                for x in loadedFile["wasteCollection"].keys():
                    if x == "Saturday":
                        collectionTuples = tuple(loadedFile["wasteCollection"]["Saturday"].items())
                        return collectionTuples
            elif valueTuple[0] == "Sunday":
                file = open(os.path.join(*path))
                loadedFile = json.load(file)
                for x in loadedFile["wasteCollection"].keys():
                    if x == "Saturday":
                        collectionTuples = tuple(loadedFile["wasteCollection"]["Sunday"].items())
                        return collectionTuples

        pygame.init()
        surface = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        menu = pygame_menu.Menu('Intelligent Garbage Truck', self.windowWidth, self.windowHeight,
                                theme=pygame_menu.themes.THEME_DARK)
        menu.add.selector('Season: ', [('Spring', 1), ('Summer', 2), ('Fall', 3), ('Winter', 4)],
                          selector_id='season_selector',
                          onchange=setSeason)  # , onchange=setSeason - changing the season
        menu.add.selector('Day: ', [('Monday', 1), ('Tuesday', 2), ('Wednesday', 3), ('Thursday', 4),
                                    ('Friday', 5), ('Saturday', 6), ('Sunday', 7)], selector_id='day_selector',
                          onchange=setDay)  # , onchange=setDay - changing the day
        menu.add.button('Start', disable)  # start the game
        menu.mainloop(surface)
