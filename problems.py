import util
from game import Directions
from game import Actions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


class SingleFoodSearchProblem(SearchProblem):
    def __init__(self, startingGameState):
        # TODO 1
        self.start = startingGameState.getPacmanPosition() #x, y
        self.walls = startingGameState.getWalls()

        self.goal = self.start
        foodGrid = startingGameState.getFood()
        if startingGameState.getNumFood() > 0:
            for i in range(foodGrid.width):
                for j in range(foodGrid.height):
                    if foodGrid[i][j]:
                        self.goal = (i, j)

        self._expanded = 0
                    

    def getStartState(self):
        # TODO 2
        return self.start

    def isGoalState(self, state):
        # TODO 3
        return state == self.goal

    def getSuccessors(self, state):
        # TODO 4
        successors = []
        directions = [Directions.NORTH, Directions.EAST, Directions.WEST, Directions.SOUTH]

        for action in directions:
            x, y = state
            dx, dy = Actions.directionToVector(action)

            nextx = int(x + dx)
            nexty = int(y + dy)

            if not self.walls[nextx][nexty]:
                nextState = (nextx, nexty)
                cost = 1
                successors.append((nextState, action, cost))

        return successors

    def getCostOfActions(self, actions):
        # TODO 5
        if actions == None: 
            return float("inf")

        x, y = self.getStartState()

        cost = 0
        for action in actions:
            dx, dy = Actions.directionToVector(action)
            x = int(x + dx)
            y = int(y + dy)
            
            if self.walls[x][y]:
                return float("inf")

            cost += 1

        return cost
        


class MultiFoodSearchProblem(SearchProblem):
    def __init__(self, startingGameState):
        self.start = (startingGameState.getPacmanPosition(), startingGameState.getFood())
        self.walls = startingGameState.getWalls()
        self.startingGameState = startingGameState
        self._expanded = 0 # DO NOT CHANGE
        self.heuristicInfo = {} # A dictionary for the heuristic to store information

    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        return state[1].count() == 0

    def getSuccessors(self, state):
        successors = []
        self._expanded += 1
        for direction in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x, y = state[0]
            dx, dy = Actions.directionToVector(direction)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextFood = state[1].copy()
                nextFood[nextx][nexty] = False
                successors.append((((nextx, nexty), nextFood), direction, 1))
        return successors

    def getCostOfActions(self, actions):
        x, y = self.getStartState()[0]
        cost = 0
        for action in actions:
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]:
                return 999999
            cost += 1
        return cost



    