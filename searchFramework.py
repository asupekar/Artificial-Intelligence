# The search algorithm itself -- it takes a problem, which will give it an initial state and the goal test,
#  the world state itself which gives it the successor states, and an evaluator that evaluates the quality
#   of a node on the search fringe

#  Client supplies
#    -- a WorldState; a WorldState implements the method successors()
#    -- a Problem which supplies the initial state and goal state checker
#    -- a costing function g([a1 ... an]) that computes the cost of a sequence of actions
#    -- a goal estimator f(s) estimating the cost from the state s to a goal
#
#    Optional parameters
#       -- verbose (integer or None) -- if not None, search will print diagnostic information
#            at the specified number of iterations
#       -- limit (integer or None) -- search will terminate after this many iterations
#           whether or not a solution was found).  If None, the search will only terminate 
#           if a solution is found or the fringe has been exhausted.
#
#   Search returns a 2-tuple -- 
#       -- a list of actions
#       -- performance information tuple  
#              number of nodes visited, 
#              process time used
#              number of nodes skipped (because they were previously expanded
#              the largest size of the fringe
#
#      The sequence of actions is None if and only if the search terminated without finding a solution,
#        either due to exhausting the fringe or due to reaching the iteration limit.

import time
import searchClientInterface

##############################################
# SearchState -- this class is used only by the search framework
# Instances of SearchState go on the search fringe -- contains both a WorldState and 
# list of actions so far.  

class SearchState:
    def __str__(self):
        return "{S " + str(self._worldState) + "/" + str(self._actions) + "}"
    
    def __init__(self, worldState, actions):
        self._worldState = worldState
        self._actions = actions
    
    def worldState(self):
        return self._worldState
    
    def actions(self):
        return self._actions
    
#############################################################
#                              
#    aStarSearch(problem, evaluator, verbose=None, limit=None)
#      *  problem -- an instance of Problem, containing the initial state
#                    (an instance of WorldState) and a goal state checker
#      *  evaluator -- an instance of Evaluator containing the functions to
#                    to evaluate a state's "quality" 
#      *  verbose=<number or None> -- if a number > 0 search will print
#                    diagnostic information to the console each <number> cycles
#                    if None, no diagnostic output
#      *  limit=<number or None> -- if a number, search will terminate with failure
#                    if no solution is found in that number of cycles.  If None, 
#                    search will continue until a solution is found or all paths are
#                    exhausted
#
#    Returns   (solution, stats)
#       * solution is a list of "actions" if a solution is found, None otherwise.
#         The type and meaning of "action" is determined by the client in the definition of WorldState
#       * stats reports performance statistic.  It is a tuple of four numbers
#              --  The amount of process time consumed by the search:  https://docs.python.org/3/library/time.html
#               -- The number of loop iterations (nodes visited)
#               -- The number of nodes skipped due to having been visited previously
#               -- Maximum size of the search fringe
#############################################################

def aStarSearch(problem, evaluator, verbose=None, limit=None):
    startTime = time.process_time()
    fringe = PriorityQueue()
    max_fringe_size = 0
    visited = {}
    
    initialWorldState = problem.initial()
    initialValue = evaluator.value(initialWorldState, [])
    initialSearchState = SearchState(initialWorldState, [])
    fringe.update(initialSearchState, initialValue)
    
    numVisited = numSkipped = 0
    while (True):
        if len(fringe.heap) > max_fringe_size:
            max_fringe_size = len(fringe.heap)
        if fringe.isEmpty():
            return (None, (time.process_time() - startTime, numVisited, numSkipped, max_fringe_size))
        nextNode = fringe.pop()   # A search state (state, actions)
        numVisited += 1
        if (limit and numVisited > limit):
            return(None, (time.process_time() - startTime, numVisited, numSkipped, max_fringe_size))
        if (verbose and numVisited % verbose == 0):
            print("Visited " + str(numVisited) + " world is " + str(nextNode._worldState))
            print("Skipped " + str(numSkipped) + " Fringe is size " + str(len(fringe.heap)))
            print("Evaluation is " + str(evaluator.value(nextNode._worldState, nextNode._actions)) + \
                  " with actions " + str(len(nextNode._actions)))
            
        if (problem.isGoal(nextNode.worldState())):
            return (nextNode._actions, (time.process_time() - startTime, numVisited, numSkipped, max_fringe_size))
        
        if (nextNode._worldState in visited):
            numSkipped += 1
        else:
            visited[nextNode.worldState()] = True
            successors = nextNode.worldState().successors()
            for successor in successors:
                state, action = successor
                actions = list(nextNode.actions())
                actions.append(action)
                newSS = SearchState(state, actions)
                newValue = evaluator.value(state, actions)
                fringe.update(newSS, newValue)
    raise "Impossible search execution path."

    #################################################
    ## Priority Queue copied directly from Berkeley AI Pacman Code 

import heapq

class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def pp(self):
        print("["),
        for entry in self.heap:
            print(entry, " "),
        print("]")
    
    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)

