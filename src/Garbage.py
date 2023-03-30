import os
import random
import re


class Garbage:
    def __init__(self):
        self.wasteList = []
        self.loadAllWaste()

    def loadBioWasteImages(self):
        self.wasteList.append(("eggshell","bio", os.path.join("..", "resources", "waste", "bio", "eggshell.jpg")))
        self.wasteList.append(("leaves","bio", os.path.join("..", "resources", "waste", "bio", "leaves.jpg")))
        self.wasteList.append(("peel","bio", os.path.join("..", "resources", "waste", "bio", "peel.jpg")))
        self.wasteList.append(("scraps","bio", os.path.join("..", "resources", "waste", "bio", "scraps.jpg")))
        self.wasteList.append(("stick","bio", os.path.join("..", "resources", "waste", "bio", "stick.jpg")))

    def loadGlassWasteImages(self):
        self.wasteList.append(("glassBottle","glass", os.path.join("..", "resources", "waste", "glass", "glassBottle.jpg")))
        self.wasteList.append(("glass","glass", os.path.join("..", "resources", "waste", "glass", "glass.jpg")))
        self.wasteList.append(("glasses","glass", os.path.join("..", "resources", "waste", "glass", "glasses.jpg")))
        self.wasteList.append(("jug","glass", os.path.join("..", "resources", "waste", "glass", "jug.jpg")))
        self.wasteList.append(("lightbulb","glass", os.path.join("..", "resources", "waste", "glass", "lightbulb.jpg")))

    def loadMetalWasteImages(self):
        self.wasteList.append(("can","metal", os.path.join("..", "resources", "waste", "metal", "can.jpg")))
        self.wasteList.append(("foil","metal", os.path.join("..", "resources", "waste", "metal", "foil.jpg")))
        self.wasteList.append(("nail","metal", os.path.join("..", "resources", "waste", "metal", "nail.jpg")))
        self.wasteList.append(("pipe","metal", os.path.join("..", "resources", "waste", "metal", "pipe.jpg")))
        self.wasteList.append(("pot","metal", os.path.join("..", "resources", "waste", "metal", "pot.jpg")))

    def loadMixedWasteImages(self):
        self.wasteList.append(("ash","mixed", os.path.join("..", "resources", "waste", "mixed", "ash.jpg")))
        self.wasteList.append(("diaper","mixed", os.path.join("..", "resources", "waste", "mixed", "diaper.jpg")))
        self.wasteList.append(("medicine","mixed", os.path.join("..", "resources", "waste", "mixed", "medicine.jpg")))
        self.wasteList.append(("syringe","mixed", os.path.join("..", "resources", "waste", "mixed", "syringe.jpg")))
        self.wasteList.append(("wetTissue","mixed", os.path.join("..", "resources", "waste", "mixed", "wetTissue.jpg")))

    def loadPaperWasteImages(self):
        self.wasteList.append(("book","paper", os.path.join("..", "resources", "waste", "paper", "book.jpg")))
        self.wasteList.append(("cardboard","paper", os.path.join("..", "resources", "waste", "paper", "cardboard.jpg")))
        self.wasteList.append(("magazine","paper", os.path.join("..", "resources", "waste", "paper", "magazine.jpg")))
        self.wasteList.append(("newspaper","paper", os.path.join("..", "resources", "waste", "paper", "newspaper.jpg")))
        self.wasteList.append(("wrapping","paper", os.path.join("..", "resources", "waste", "paper", "wrapping.jpg")))

    def loadPlasticWasteImages(self):
        self.wasteList.append(("plasticBottle","plastic", os.path.join("..", "resources", "waste", "plastic", "plasticBottle.jpg")))
        self.wasteList.append(("container","plastic", os.path.join("..", "resources", "waste", "plastic", "container.jpg")))
        self.wasteList.append(("packaging","plastic", os.path.join("..", "resources", "waste", "plastic", "packaging.jpg")))
        self.wasteList.append(("straw","plastic", os.path.join("..", "resources", "waste", "plastic", "straw.jpg")))
        self.wasteList.append(("toy","plastic", os.path.join("..", "resources", "waste", "plastic", "toy.jpg")))

    def loadAllWaste(self):
        self.loadPlasticWasteImages()
        self.loadPaperWasteImages()
        self.loadMixedWasteImages()
        self.loadMetalWasteImages()
        self.loadGlassWasteImages()
        self.loadBioWasteImages()

    # containers will hold up to 7 random pieces of waste
    def getRandomWaste(self):
        randomIndexList = random.sample(range(0, len(self.wasteList)), 7)
        randomWasteList = []
        for index in randomIndexList:
            randomWasteList.append(self.wasteList[index])
        return randomWasteList
