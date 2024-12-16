# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # use a stack as the main data structure to ensure LIFO order needed for DFS
    from util import Stack
    
    stack = Stack() 
    state = problem.getStartState()
    stack.push((state, []))
    
    tempList  = []
    visitedStates = set()
    # iterate over the stack, pushing successors onto the stack if the current state is not the goal state
    while not stack.isEmpty():
        currentStateTuple = stack.pop()
        currentState, currentList = currentStateTuple
        
        if problem.isGoalState(currentState):
            return currentList
        
        if currentState not in visitedStates: 
            visitedStates.add(currentState)
            
            tempList = problem.getSuccessors(currentState)
        
            for tempState in tempList:
                if tempState[0] not in visitedStates:
                    stack.push((tempState[0], currentList + [tempState[1]]))
            
            
    return []
           

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    # use queue as main data structure to implement FIFO order needed for BFS
    queue = Queue()
    state = problem.getStartState()
    queue.push((state, []))
    
    tempList = []
    visitedStates = set()
    
    # iterate over the queue, queueing successors into the queue if the current state is not the goal state
    while not queue.isEmpty():
        currentStateTuple = queue.pop()
                
        currentState, currentList = currentStateTuple
        if problem.isGoalState(currentState):
            return currentList
        
        if currentState not in visitedStates: 
            visitedStates.add(currentState)
            
            tempList = problem.getSuccessors(currentState)
        
            for tempState in tempList:
                if tempState[0] not in visitedStates:
                    queue.push((tempState[0], currentList + [tempState[1]]))
    # return empty list if it fails
    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue
    # PriorityQueue gebruikt om de node met de laagste f(n) te selecteren
    frontier = PriorityQueue()
    start_state = problem.getStartState()
    frontier.push((start_state, [], 0), 0)  # (state, actions, cost)

    explored = set()

    while not frontier.isEmpty():
        current_state, actions, current_cost = frontier.pop()

        if problem.isGoalState(current_state):
            return actions

        if current_state not in explored:
            explored.add(current_state)

            for successor, action, step_cost in problem.getSuccessors(current_state):
                if successor not in explored:
                    new_cost = current_cost + step_cost
                    f_cost = new_cost + heuristic(successor, problem)
                    frontier.push((successor, actions + [action], new_cost), f_cost)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
