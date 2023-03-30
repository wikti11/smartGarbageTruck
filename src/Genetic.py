import random
from src.Astar import Astar
from src.Agent import State

class Genetic:
    def __init__(self, environment, initialState, unvisitedHouses,destinationStates, agent):
        self.environment = environment
        self.initialState = initialState
        self.unvisitedHouses = unvisitedHouses
        self.destinationStates = destinationStates
        self.agent = agent

    def addToGen(self,initialState, unvisitedHouses, newGeneration):
        cost = 0
        for house in unvisitedHouses:
            if isinstance(house, int):
                print("haloe")
            destX = house[0]
            destY = house[1]
            self.destinationStates.append(State(self.environment, destX, destY))
        while self.destinationStates:
            destinationState = self.destinationStates.pop(0)
            sol = Astar(self.environment, initialState, destinationState, self.agent).solve()
            initialState = sol[0][-1][0]
            cost = cost + sol[1]
        newGeneration.append((unvisitedHouses, cost))


    def mate(self, parent1, parent2):
        cutoff1 = random.randint(0, len(parent1) - 1)
        cutoff2 = random.randint(cutoff1 + 1, len(parent1))
        child1 = [0]*len(parent1)
        #child2 = []
        insert =[]
        for i in range(len(parent1)):
            if (parent1[i] not in parent2[cutoff1:cutoff2]):
                child1[i]=parent1[i]
        child1[cutoff1:cutoff2] = parent2[cutoff1:cutoff2]
        for i in range(len(child1)):
            if child1[i]==0:
                for x in parent1:
                    if x not in child1:
                        child1[i]=x
        return child1

        # count = 0
        # for i in partner:
        #     if (count == cutoff1):
        #         break
        #     if (i not in self[cutoff1:cutoff2]):
        #         child2.append(i)
        #         count = count + 1
        # child2.extend(self[cutoff1:cutoff2])
        # child2.extend([x for x in partner if x not in child2])


    def mutate(self,thing):
        if random.random() <= 0.01:
            lenght = len(thing)
            a = random.randrange(0, lenght, 1)
            b = random.randrange(0, lenght, 1)
            while a == b:
                b = random.randrange(0, lenght, 1)
            thing[a], thing[b] = thing[b], thing[a]
        return thing

    def solve(self):
        popSize = 20
        population = []
        destinationStates = []
        newGeneration = []
        half = int(popSize / 2)
        gen = 1
        cost = 0
        for i in range(popSize):
            random.shuffle(self.unvisitedHouses)
            shuffle = self.unvisitedHouses.copy()
            initialState = self.agent.state
            for house in self.unvisitedHouses:
                destX = house[0]
                destY = house[1]
                destinationStates.append(State(self.environment, destX, destY))
            while destinationStates:
                destinationState=destinationStates.pop(0)
                sol = Astar(self.environment, initialState,destinationState , self.agent).solve()
                initialState = sol[0][-1][0]
                cost = cost + sol[1]
            population.append((shuffle, cost))
            cost = 0
        while gen != 10:
            population.sort(key=lambda x: x[1])
            print("Generation: ",gen)
            for i in population:
                print(i, sep="\n")
            newGeneration.extend(population[:half])
            for x in range(int(half / 2)):
                parent1 = random.choice(population[:half])[0]
                parent2 = random.choice(population[:half])[0]
                while parent1 == parent2:
                    parent2 = random.choice(population[:half])[0]
                child = self.mate(parent1, parent2)
                self.mutate(child)
                self.addToGen(initialState, child, newGeneration)
                child = self.mate(parent2, parent1)
                self.mutate(child)
                self.addToGen(initialState, child, newGeneration)
            population = newGeneration
            newGeneration = []
            gen += 1
        population.sort(key=lambda x: x[1])
        return population[0]