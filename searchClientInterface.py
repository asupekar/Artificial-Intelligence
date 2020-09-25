#####################################################################
##  Interfaces that must be implemented by the client

#####
# WorldState -- all information needed to check for goal and to generate 
#    successor states
#
#  Method successors() must return a list of tuples:  (worldState, action)
#    -- the data type of action is up to the client
# 
# * Implementation must be aware that it is going to be stored and compared
#      against other states:  override hash and equals appropriately
# * Implementation must not share mutable state across instances!

class WorldState:
	def successors():
		raise "Not implemented"
		
#############################################
# Problem -- must supply the initial state and a goal state checker   
	
class Problem:
	# Method initial returns a WorldState or subclass
	def initial(self):
		raise "Not implemented"
		
	# Method isGoal returns a boolean
	def isGoal(self, state):
		raise "Not implemented"

#############################################
# Evaluator
#    Client provides g(s) and h*(s) in the form of actionsCoster and goalEstimator      
#    Evaluator superclass provides the evaluator f*(s) = g(s) + h*(s)

class Evaluator:
	def __init__(self, actionsCoster, goalEstimator):
		self._coster = actionsCoster
		self._estimator = goalEstimator
	def value(self, state, actions):
		return self._coster(actions) + self._estimator(state)

#####  Specific evaluators for breadth-first and depth-first search

class BFSEvaluator(Evaluator):
	def __init__(self):
		super().__init__(lambda actions: len(actions), lambda _: 0)
	 

class DFSEvaluator(Evaluator):
	def __init__(self):
		super().__init__(lambda actions: -len(actions), lambda _:0)

######################################################################
