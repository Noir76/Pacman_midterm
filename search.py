"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from game import Directions
import util

n = Directions.NORTH
s = Directions.SOUTH
e = Directions.EAST
w = Directions.WEST


def depthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 17
    initState = problem.getStartState()
    
    frontier = util.Stack()

    explored = []

    frontier.push((initState, [], 0))

    while frontier:
        curState, curAct, curCost = frontier.last()
        if curState not in explored:
            explored.append(curState)

        if problem.isGoalState(curState):
            return curAct
        
        childs = problem.getSuccessors(curState)
        moveable = True

        for child in childs:
            childState, childAct, childCost = child
            
            if childState not in explored:
                toltalAct = curAct + [childAct]
                totalCost = curCost + childCost
                frontier.push((childState, toltalAct, totalCost))
                moveable = False
                break

        if moveable:
            frontier.pop()

    return curAct


def breadthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 18
    """Search the shallowest nodes in the search tree first."""
    initState = problem.getStartState()
    
    frontier = util.Queue()

    explored = []

    frontier.push((initState, [], 0))

    while frontier:
        curState, curAct, curCost = frontier.pop()
        
        if curState not in explored:
            explored.append(curState)

            if problem.isGoalState(curState):
                return curAct
            
            childs = problem.getSuccessors(curState)

            for child in childs:
                childState, childAct, childCost = child
                
                toltalAct = curAct + [childAct]
                totalCost = curCost + childCost
                
                frontier.push((childState, toltalAct, totalCost))

    return curAct
    


def uniformCostSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 19
    initState = problem.getStartState()
    
    frontier = util.PriorityQueue()

    explored = []

    frontier.push((initState, [], 0), 0)

    while frontier:
        curState, curAct, curCost = frontier.pop()
        
        if problem.isGoalState(curState):
            return curAct
        
        if curState not in explored:
            explored.append(curState)

            childs = problem.getSuccessors(curState)

            for child in childs:
                childState, childAct, childCost = child
                toltalAct = curAct + [childAct]
                totalCost = curCost + childCost

                frontier.update((childState, toltalAct, totalCost), totalCost)

    return curAct

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def singleFoodSearchHeuristic(state, problem=None):
    """
    A heuristic function for the problem of single food search
    """
    # TODO 20
    pacman_pos = state 
    food_pos = problem.goal
    return abs(pacman_pos[0] - food_pos[0])+abs(pacman_pos[1] - food_pos[1])


def multiFoodSearchHeuristic(state, problem=None):
    """
    A heuristic function for the problem of multi-food search
    """
    # TODO 21
    pacman_pos = state 
    food_list = problem.food.asList()
    if food_list.empty():
        return 0
    
    result = 0
    for food in food_list:
        dist = abs(pacman_pos[0] - food[0])+abs(pacman_pos[1] - food[1])
        result = sum(result, dist)

    return result


def aStarSearch(problem, heuristic=nullHeuristic):
    '''
    return a path to the goal
    '''
    # TODO 22
    initState = problem.getStartState()
    
    frontier = util.PriorityQueue()

    explored = []

    frontier.push((initState, [], 0), 0)

    while frontier:
        curState, curAct, curCost = frontier.pop()
        
        if problem.isGoalState(curState):
            return curAct
        
        if curState not in explored:
            explored.append(curState)

            childs = problem.getSuccessors(curState)

            for child in childs:
                childState, childAct, childCost = child
                toltalAct = curAct + [childAct]
                totalCost = curCost + childCost
                priority = totalCost + heuristic(childState, problem)

                frontier.update((childState, toltalAct, totalCost), priority)

    return curAct

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
