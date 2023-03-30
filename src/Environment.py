class Environment:
    def __init__(self, rows, columns, garbageTruck, garbageDump, houses, trees, asphaltRoads, gravelRoads):
        self.rows = rows
        self.columns = columns
        self.garbageTruck = garbageTruck
        self.garbageDump = garbageDump
        self.houses = houses
        self.trees = trees
        self.asphaltRoads = asphaltRoads
        self.gravelRoads = gravelRoads
        self.entities = []
        self.entities.append(garbageTruck)
        self.entities.append(garbageDump)
        self.entities.extend(houses)
        self.entities.extend(trees)
        self.entities.extend(asphaltRoads)
        self.entities.extend(gravelRoads)

    def getEntityByPos(self, x, y):
        for entity in self.entities:
            if entity.posX == x and entity.posY == y:
                return entity
        return None

    def getHouseByPos(self, x, y): # cause getEntityByPos returns Truck if Truck and House are on same coords
        for h in self.houses:
            if h.posX == x and h.posY == y:
                return h
        return None