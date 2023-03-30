class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action


class Problem:
    def __init__(self, environment, initialState, destinationState, agent):
        self.initialState = initialState
        self.destinationState = destinationState
        self.environment = environment
        self.agent = agent

    def solve(self):
        fringe = []
        explored = []
        fringe.append(Node(self.initialState))
        while fringe:
            elem = fringe.pop()
            if self.goalTest(elem.state):
                solution = [(elem.state, elem.action)]
                while elem.parent is not None:
                    elem = elem.parent
                    if elem.action is not None:
                        solution.append((elem.state, elem.action))
                return solution
            explored.append(elem)
            for state, action in elem.state.successors():
                if not any(n.state == state for n in fringe) and not any(n.state == state for n in explored):
                    fringe.append(Node(state, elem, action))

        return None

    def goalTest(self, state):
        if state == self.destinationState:
            return True
        return False
