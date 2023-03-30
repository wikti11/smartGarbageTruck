class EnvironmentEntity:
    def __init__(self, posX, posY, rotation=None):
        self.posX = posX
        self.posY = posY
        self.rotation = rotation

    def setPos(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def setRotation(self, rotation):
        self.rotation = rotation


class GarbageTruck(EnvironmentEntity):
    def __init__(self, posX, posY, rotation):
        super().__init__(posX, posY, rotation)
        self.bioWasteList = []
        self.glassWasteList = []
        self.metalWasteList = []
        self.paperWasteList = []
        self.plasticWasteList = []
        self.mixedWasteList = []
        self.filling = 0
        self.maxFilling = 5

    def addWaste(self, waste, category):
        if category == "bio":
            self.bioWasteList.append(waste)
        elif category == "glass":
            self.glassWasteList.append(waste)
        elif category == "metal":
            self.metalWasteList.append(waste)
        elif category == "paper":
            self.paperWasteList.append(waste)
        elif category == "plastic":
            self.plasticWasteList.append(waste)
        elif category == "mixed":
            self.mixedWasteList.append(waste)
        self.filling = self.filling + 1

    def getAllWaste(self):
        allWasteList = []
        allWasteList.extend(self.bioWasteList)
        allWasteList.extend(self.glassWasteList)
        allWasteList.extend(self.metalWasteList)
        allWasteList.extend(self.paperWasteList)
        allWasteList.extend(self.plasticWasteList)
        allWasteList.extend(self.mixedWasteList)
        return allWasteList

    def clearAllWaste(self):
        self.bioWasteList.clear()
        self.glassWasteList.clear()
        self.metalWasteList.clear()
        self.paperWasteList.clear()
        self.plasticWasteList.clear()
        self.mixedWasteList.clear()
        self.filling = 0


class GarbageDump(EnvironmentEntity):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.wasteList = []

    def addWasteList(self, wasteList):
        self.wasteList.extend(wasteList)


class House(EnvironmentEntity):
    def __init__(self, posX, posY, wasteList):
        super().__init__(posX, posY)
        self.wasteList = wasteList
        self.filling = len(wasteList)

    def getWasteList(self):
        return self.wasteList

    def removeWaste(self, waste):
        self.wasteList.remove(waste)
        self.filling = self.filling - 1


class Tree(EnvironmentEntity):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)


class AsphaltRoad(EnvironmentEntity):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)


class GravelRoad(EnvironmentEntity):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
