import random

from game import Agent
from game import Directions
import search
import problems
class GoWestAgent(Agent):
    def getAction(self, state):
        if Directions.WEST in state.getLegalPacmanActions():
            return Directions.WEST
        else:
            return Directions.STOP


class RandomAgent(Agent):
    def getAction(self, state):
        actions = state.getLegalPacmanActions()
        random.shuffle(actions)
        return actions[0]


class SearchAgent(Agent):
    def registerInitialState(self, state):
        """
        This is the first time that the agent sees the layout of the game
        board. Here, we choose a path to the goal. In this phase, the agent
        should compute the path to the goal and store it in a local variable.
        All of the work is done in this method!

        state: a GameState object (pacman.py)
        """
        # TODO 11
        problem = self.searchType(state)
        self.actions = self.searchFunction(problem)
        cost = problem.getCostOfActions(self.actions)
        print("Total cost of path:", cost)

    def getAction(self, state):
        """
        Returns the next action in the path chosen earlier (in
        registerInitialState).  Return Directions.STOP if there is no further
        action to take.

        state: a GameState object (pacman.py)
        """
        # TODO 12
        if 'index' not in dir(self): 
            self.index = 0
        else:
            self.index += 1

        if self.index < len(self.actions) and state.getNumFood() > 0:
            return self.actions[self.index]
        else:
            return Directions.STOP


class BFSFoodSearchAgent(SearchAgent):
    # TODO 13
    def __init__(self, prob):
        self.searchFunction = search.bfs
        self.searchType = getattr(problems, prob)


class DFSFoodSearchAgent(SearchAgent):
    # TODO 14
    def __init__(self, prob):
        self.searchFunction = search.dfs
        self.searchType = getattr(problems, prob)


class UCSFoodSearchAgent(SearchAgent):
    # TODO 15
     def __init__(self, prob):
        self.searchFunction = search.ucs
        self.searchType = getattr(problems, prob)


class AStarFoodSearchAgent(SearchAgent):
    # TODO 16
     def __init__(self, prob):
        self.searchFunction = search.astar
        self.searchType = getattr(problems, prob)
