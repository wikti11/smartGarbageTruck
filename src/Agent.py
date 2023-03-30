import math

import numpy as np

from src.Entities import AsphaltRoad, GravelRoad, GarbageDump, House


class Agent:
    def __init__(self, environment, entity):
        self.environment = environment
        self.entity = entity
        self.state = State(self.environment, self.entity.posX, self.entity.posY, self.entity.rotation)

    def applyAction(self, action):
        if action is not None:
            self.state = action(self.state)
            self.entity.posX = self.state.posX
            self.entity.posY = self.state.posY
            self.entity.rotation = self.state.rotation

class State:
    def __init__(self, environment, posX, posY, rotation=None):
        self.environment = environment
        self.posX = posX
        self.posY = posY
        self.rotation = rotation

    def __eq__(self, other):
        return self.posY == other.posY and self.posX == other.posX and (
                    self.rotation == other.rotation or self.rotation is None or other.rotation is None)

    def successors(self):
        result = []

        if self.rotation is not None:
            forwardX = self.posX + 1 * int(np.cos(np.deg2rad(self.rotation)))
            forwardY = self.posY - 1 * int(np.sin(np.deg2rad(self.rotation)))
            forwardEntity = self.environment.getEntityByPos(forwardX, forwardY)
            if isinstance(forwardEntity, AsphaltRoad) or isinstance(forwardEntity, GravelRoad)\
                    or isinstance(forwardEntity, GarbageDump) or isinstance(forwardEntity, House) or forwardEntity is None:
                result.append((Actions.goForward(self), Actions.goForward, forwardEntity))
            result.append((Actions.turnRight(self), Actions.turnRight, None))

            result.append((Actions.turnLeft(self), Actions.turnLeft, None))
        else:
            print("Rotation required in state to find successors.")

        return result


class Actions:
    def __init__(self):
        self.goForward = self.goForward
        self.turnLeft = self.turnLeft
        self.turnRight = self.turnRight

    @staticmethod
    def goForward(state):
        if state.rotation is not None:
            forwardX = state.posX + 1 * int(np.cos(np.deg2rad(state.rotation)))
            forwardY = state.posY - 1 * int(np.sin(np.deg2rad(state.rotation)))
            return State(state.environment, forwardX, forwardY, state.rotation)
        else:
            print("Rotation field required in state to plan action.")
            return state

    @staticmethod
    def turnRight(state):
        if state.rotation is not None:
            rotation = math.fmod(state.rotation - 90, 360)
            if rotation < 0:
                rotation = 360 + rotation
            return State(state.environment, state.posX, state.posY, rotation)
        else:
            print("Rotation field required in state to plan action.")
            return state

    @staticmethod
    def turnLeft(state):
        if state.rotation is not None:
            rotation = math.fmod(state.rotation + 90, 360)
            return State(state.environment, state.posX, state.posY, rotation)
        else:
            print("Rotation field required in state to plan action.")
            return state
