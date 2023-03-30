import math
import time

import pygame
import random

from src import DecisionTree
from src.Agent import State
from src.Entities import GarbageTruck, GarbageDump, House, Tree, AsphaltRoad, GravelRoad
from src.Problem import Problem
from src.Project import Project
from src.Astar import Astar
from src.NeuralNetwork import NeuralNetwork
from src.Genetic import Genetic

# from src.DecisionTree import DecisionTree

def displayEnvironment():
    project.game.window.fill((0, 255, 0))
    # ground layer
    for i in range(project.environment.columns):
        for j in range(project.environment.rows):
            entityImage = project.game.grassImage
            for e in project.environment.entities:
                if e.posX == i and e.posY == j:
                    if isinstance(e, AsphaltRoad):
                        entityImage = project.game.asphaltRoadImage
                    elif isinstance(e, GravelRoad):
                        entityImage = project.game.gravelRoadImage
            project.game.window.blit(entityImage, (i * project.game.fieldWidth, j * project.game.fieldHeight))
    # entity layer
    for i in range(project.environment.columns):
        for j in range(project.environment.rows):
            entityImage = project.game.emptyImage
            for e in project.environment.entities:
                if e.posX == i and e.posY == j:
                    if isinstance(e, GarbageTruck):
                        entityImage = project.game.garbageTruckImage
                        if project.environment.garbageTruck.rotation == 0:
                            entityImage = pygame.transform.flip(project.game.garbageTruckImage,
                                                                True, False)
                        elif project.environment.garbageTruck.rotation == 270 or project.environment.garbageTruck.rotation == 90:
                            entityImage = pygame.transform.flip(project.game.garbageTruckImage,
                                                                True, False)
                            entityImage = pygame.transform.rotate(entityImage,
                                                                  project.environment.garbageTruck.rotation)
                    elif isinstance(e, GarbageDump):
                        entityImage = project.game.garbageDumpImage
                    elif isinstance(e, House):
                        entityImage = project.game.houseImage1
                    elif isinstance(e, Tree):
                        entityImage = project.game.treeImage
            project.game.window.blit(entityImage, (i * project.game.fieldWidth, j * project.game.fieldHeight))
    pygame.display.update()

lastVisitedHouseNum = -1

def returnUnvisitedHouses():
    unvisitedHouses = []
    for i in range(project.environment.columns):
        for j in range(project.environment.rows):
            for e in project.environment.entities:
                if e.posX == i and e.posY == j:
                    if isinstance(e, House):
                        coords = []
                        coords.append(e.posX)
                        coords.append(e.posY)
                        tupledCoords = tuple(coords)
                        unvisitedHouses.append(tupledCoords)
    return unvisitedHouses
def UnvisitedHousesCoords():
    destinationStates = []
    for x in range(len(returnUnvisitedHouses())):
        destX = returnUnvisitedHouses()[x][0]
        destY = returnUnvisitedHouses()[x][1]
        destinationStates.append(State(project.environment, destX, destY))

    return destinationStates

def handleEvents():
    global lastVisitedHouseNum
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            project.game.isRunning = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                try:
                    project.agent.applyAction(project.solution[0].pop()[1])
                    if not project.solution[0]:
                        project.agent.state = State(project.environment, project.agent.state.posX, project.agent.state.posY, math.fmod(project.agent.state.rotation + 180, 360))
                    displayEnvironment()
                except IndexError:
                    print("No more actions left.")
                except AttributeError:
                    print("Destination unreachable or not marked.")

            initialState = project.agent.state
            #houseToVisit = UnvisitedHousesCoords()[0]
            #houseToVisit = project.environment.houses[(lastVisitedHouseNum + 1) % len(project.environment.houses)]
            #UnvisitedHouses1 = Genetic(project.environment, initialState, returnUnvisitedHouses(), UnvisitedHousesCoords(), project.agent).solve()
            houseToVisitCoords = HousesToVisit[0][lastVisitedHouseNum + 1]
            if project.agent.state.posX == project.environment.garbageDump.posX and project.agent.state.posY == project.environment.garbageDump.posY:
                print(f"Arrived at Garbage Dump.")
                project.environment.garbageTruck.clearAllWaste()

                houseToVisitCoords = HousesToVisit[0][lastVisitedHouseNum + 1]
                #houseToVisit = project.environment.houses[(lastVisitedHouseNum + 1) % len(project.environment.houses)]

                destState = State(project.environment, houseToVisitCoords[0], houseToVisitCoords[1])
                project.solution = Astar(project.environment, initialState, destState,
                                         project.agent).solve()
            if project.agent.state.posX == houseToVisitCoords[0] and project.agent.state.posY == houseToVisitCoords[1]:
                houseToVisit = project.environment.getHouseByPos(houseToVisitCoords[0], houseToVisitCoords[1])
                print(f"Arrived at House {[w[0] for w in houseToVisit.getWasteList()]}")
                for w in houseToVisit.getWasteList():
                    #wasteCategory = w[1]

                    image = pygame.transform.scale(pygame.image.load(w[2]), (project.game.fieldWidth, project.game.fieldHeight))
                    project.game.window.blit(image, (project.game.fieldWidth * houseToVisitCoords[0], project.game.fieldHeight * houseToVisitCoords[1]))
                    pygame.display.update()


                    wasteCategory=neuralNetwork.classifyImage(w[2])
                    if DecisionTree.predict(project.game.selectedDay, project.game.selectedSeason, houseToVisit.filling, wasteCategory, project.environment.garbageTruck.filling):
                        print(f"Loaded on truck: {w[0]} ({wasteCategory}).")
                        project.environment.garbageTruck.addWaste(w, wasteCategory)
                        houseToVisit.removeWaste(w)
                        print(f"Truck filling: {project.environment.garbageTruck.filling}")
                        if project.environment.garbageTruck.filling >= project.environment.garbageTruck.maxFilling:
                            break

                    time.sleep(1)
                    displayEnvironment()
                if project.environment.garbageTruck.filling >= project.environment.garbageTruck.maxFilling:
                    print("Truck is full, heading to the Garbage Dump.")
                    destState = State(project.environment, project.environment.garbageDump.posX, project.environment.garbageDump.posY)
                else:
                    lastVisitedHouseNum = lastVisitedHouseNum + 1
                    if lastVisitedHouseNum + 1 < len(project.environment.houses):
                        houseToVisitCoords = HousesToVisit[0][lastVisitedHouseNum+1]
                        #houseToVisit = project.environment.houses[(lastVisitedHouseNum + 1) % len(project.environment.houses)]
                        destState = State(project.environment, houseToVisitCoords[0], houseToVisitCoords[1])
                    else:
                        print("All of the houses are visited, heading to the Garbage Dump.")
                        destState = State(project.environment, project.environment.garbageDump.posX, project.environment.garbageDump.posY)
                project.solution = Astar(project.environment, initialState, destState,
                                         project.agent).solve()

            # if project.agent.state in UnvisitedHousesCoords() and (UnvisitedHousesCoords().index(project.agent.state)+1)<= len(UnvisitedHousesCoords()):
            #     if getHousesWithWaste():
            #         houseToVisit = getHousesWithWaste()[lastVisitedHouseNum+1 % len(getHousesWithWaste())]
            #         destState = houseToVisit.posX, houseToVisit.posY
            #         print(destState.posX, destState.posY)
            #         print(initialState.posX, initialState.posY)
            #         project.solution = Astar(project.environment, initialState, destState, project.agent).solve()
            #
            # else:
            #     project.solution = Astar(project.environment, initialState,  UnvisitedHousesCoords()[0], project.agent).solve()

            # somehow make it that if project.agent.state == destinationStates[x], then it changes destination to destinationStates[x+1]

            # destX = pygame.mouse.get_pos()[0] // project.fieldWidth
            # destY = pygame.mouse.get_pos()[1] // project.fieldHeight
            # destinationState = State(project.environment, destX, destY)
            # print("New destination marked (" + str(destX) + ", " + str(destY) + ")")
            # project.solution = Astar(project.environment, initialState, destinationState, project.agent).solve()


if __name__ == '__main__':
    project = Project("Intelligent Garbage Truck", 60, 60)
    project.game.loadImages()
    project.game.menu()
    initialState = project.agent.state
    HousesToVisit = Genetic(project.environment, initialState, returnUnvisitedHouses(), UnvisitedHousesCoords(),
                               project.agent).solve()
    destState = State(project.environment, HousesToVisit[0][0][0], HousesToVisit[0][0][1])
    project.solution = Astar(project.environment, initialState, destState, project.agent).solve()
    neuralNetwork=NeuralNetwork()
    neuralNetwork.loadCheckpoint()
    while project.game.isRunning:
        displayEnvironment()
        handleEvents()
    project.game.endGame()
