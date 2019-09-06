class Automaton():
	"""This class stores all the information obtained in the json doc"""
	statePaht = []
	pile = []
	transitionPath = []


	def __init__(self, rawAutomaton):
		#this is a char
		self.initialState = rawAutomaton["Initial State"]
		#this is a list
		self.setOfStates = rawAutomaton["Set Of States"]
		#this is a list
		self.alphabet = rawAutomaton["Alphabet"]
		#this is a complex dictionary
		self.transitions = rawAutomaton["Transitions"]
		#this is a list
		self.setOfFinalStates = rawAutomaton["Set Of Final States"]
		#this is a list
		self.stringsToEvaluate = rawAutomaton["Strings To Evaluate"]
		#this is were the initial symbol has come 
		self.pile = ["!"]

		for string in self.stringsToEvaluate:
			print ("Eval string:", string)
			eval_string(self,string)



def eval_string(self, stringToEval):

	for transition in self.transitions[self.initialState]:
		self.pile.insert(0,transition[3])
		self.actualState = transition[2]

	errorFlag = True

	for char in stringToEval:
		if eval_char(self,char) == True:
			continue
		else:
			errorFlag = False
			break

	if self.pile[0] == "!" and errorFlag == True:
		print ("---------------- La cadena:", stringToEval, "si pertenece al lenguaje. ----------------")
	else:
		print ("---------------- La cadena:", stringToEval,"no pertenece al lenguaje. ----------------")
		
def insert_string(self, toInsert):
	for char in toInsert:
		self.pile.insert(0,char)

def eval_char(self, char):
	canPop = True
	while canPop:
		canPop = False

		for transition in self.transitions[self.actualState]:
			if transition[0] == char and transition[0] != "":  
				if transition[1] == self.pile[0]: # Can consume and can pop the pile
					print ("Can pop in trnasition:",transition)
					self.pile.remove(transition[1]) #remove pile
					if transition[3] != "":
						insert_string(self, transition[3])
					self.actualState = transition[2]
					return True

		for transition in self.transitions[self.actualState]:
			if len(transition[3]) > 1:
				if transition[3][0] == char and self.pile[0] == transition[1]: #can pop the pile and insert the char
					print("Maybe this one:",transition)
					canPop = True
					self.pile.remove(transition[1])
					insert_string(self, transition[3])
					self.actualState = transition[2]
					continue
			else:
				if transition[3] == char and self.pile[0] == transition[1]: #can pop the pile and insert the char
					canPop = True
					print("Maybe this one:",transition)
					self.pile.remove(transition[1])
					if transition[3] != "":
						insert_string(self, transition[3])
					self.actualState = transition[2]
					continue
		print("Did we pop?",canPop)
	print("Bye")
	return False

