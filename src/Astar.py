import heapq

from src.Agent import Actions
from typing import List, Tuple, TypeVar
from src.Entities import AsphaltRoad, GravelRoad, GarbageDump, House

T = TypeVar('T')

class PriorityQueue:
    def __init__(self):
        self.elements: List[Tuple[T, float]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> T:
        return heapq.heappop(self.elements)[1]


class Node:
    def __init__(self, state, parent=None, action=None, forwardEntity=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.forwardEntity = forwardEntity
        self.cost = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __eq__(self, other):
        return self.state == other.state and self.action == other.action


class Astar:
    def __init__(self, environment, initialState, destinationState, agent):
        self.initialState = initialState
        self.destinationState = destinationState
        self.environment = environment
        self.agent = agent

    def heuristic(self, state) -> float:
        return abs(state.posX-self.destinationState.posX) \
               + abs(state.posY-self.destinationState.posY)

    def goalTest(self, currentNode):
        if currentNode.state == self.destinationState:
            solution = [(currentNode.state, currentNode.action)]
            while currentNode.parent is not None:
                currentNode = currentNode.parent
                if currentNode.action is not None:
                    solution.append((currentNode.state, currentNode.action))
            return solution

    def costEval(self, action, forwardEntity):
        if action == Actions.goForward:
            if isinstance(forwardEntity, House):
                return 3
            if isinstance(forwardEntity, AsphaltRoad):
                return 1
            if isinstance(forwardEntity, GarbageDump):
                return 3
            if isinstance(forwardEntity, GravelRoad):
                return 5
            if forwardEntity is None:
                return 10
        elif action == Actions.turnLeft:
            return 2
        elif action == Actions.turnRight:
            return 2

    def solve(self):
        fringe = PriorityQueue()
        fringe.put(Node(self.initialState), 0)
        explored = []
        while fringe:
            currentNode = fringe.get()
            openStates = [currentNode.state]
            solution = self.goalTest(currentNode)
            if solution:
                return solution, currentNode.cost
            explored.append(currentNode)
            openStates.remove(currentNode.state)
            for s in currentNode.state.successors():
                child = Node(s[0], currentNode, s[1], s[2])
                if child in explored:
                    continue
                child.cost = currentNode.cost + self.costEval(child.action, child.forwardEntity)
                child.h = self.heuristic(child.state)
                child.f = child.cost + child.h
                if child.state in openStates:
                    if child.cost > currentNode.cost:
                        continue
                fringe.put(child, child.f)
                openStates.append(child.state)

        return None