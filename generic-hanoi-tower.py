from array import array
from collections import deque


peg1 = input().split()
peg2 = input().split()
peg3 = input().split()

class State:
	def __init__(self, listState, parent):
		self.listState = listState
		self.parent = parent

	def Print(self):
		for i in range(3):
			print(*self.listState[i], end='\n')
		print('#')


for i in range(len(peg1)):
	peg1[i] = int(peg1[i])
for i in range(len(peg2)):
	peg2[i] = int(peg2[i])
for i in range(len(peg3)):
	peg3[i] = int(peg3[i])

numberOfDisk = len(peg1) + len(peg2) + len(peg3)

inital_state = [array('H', peg1), array('H', peg2), array('H', peg3)]
goal = [array('H', []), array('H', [])]
temp = array('H', range(numberOfDisk-1, -1, -1))

goal.append(temp)
startState = State(inital_state, None)

def GetNeighbourState(state, explored):
	listNewState = []
	currentList = state.listState

	try:
		topDisk1 = currentList[0][-1]
	except IndexError:
		topDisk1 = -1
	try:
		topDisk2 = currentList[1][-1]
	except IndexError:
		topDisk2 = -1
	try:
		topDisk3 = currentList[2][-1]
	except IndexError:
		topDisk3 = -1

	#Peg 1
	if topDisk1 != -1:
		if topDisk2 == -1 or topDisk1 < topDisk2:
			currentList[0].pop()
			currentList[1].append(topDisk1)
			value = (tuple(currentList[0]), tuple(currentList[1]), tuple(currentList[2]))

			if value not in explored.keys():
				newState = [x[:] for x in currentList]
				listNewState.append(State(newState, state))
				explored[value] = True

			currentList[1].pop()
			currentList[0].append(topDisk1)

		if topDisk3 == -1 or topDisk1 < topDisk3:
			currentList[0].pop()
			currentList[2].append(topDisk1)
			value = (tuple(currentList[0]), tuple(currentList[1]), tuple(currentList[2]))

			if value not in explored.keys():
				newState = [x[:] for x in currentList]
				listNewState.append(State(newState, state))
				explored[value] = True

			currentList[2].pop()
			currentList[0].append(topDisk1)

	#Peg 2
	if topDisk2 != -1:
		if topDisk1 == -1 or topDisk2 < topDisk1:
			currentList[1].pop()
			currentList[0].append(topDisk2)
			value = (tuple(currentList[0]), tuple(currentList[1]), tuple(currentList[2]))

			if value not in explored.keys():
				newState = [x[:] for x in currentList]
				listNewState.append(State(newState, state))
				explored[value] = True

			currentList[0].pop()
			currentList[1].append(topDisk2)

		if topDisk3 == -1 or topDisk2 < topDisk3:
			currentList[1].pop()
			currentList[2].append(topDisk2)
			value = (tuple(currentList[0]), tuple(currentList[1]), tuple(currentList[2]))

			if value not in explored.keys():
				newState = [x[:] for x in currentList]
				listNewState.append(State(newState, state))
				explored[value] = True

			currentList[2].pop()
			currentList[1].append(topDisk2)

	#Peg 3
	if topDisk3 != -1:
		if topDisk1 == -1 or topDisk3 < topDisk1:
			currentList[2].pop()
			currentList[0].append(topDisk3)
			value = (tuple(currentList[0]), tuple(currentList[1]), tuple(currentList[2]))

			if value not in explored.keys():
				newState = [x[:] for x in currentList]
				listNewState.append(State(newState, state))
				explored[value] = True

			currentList[0].pop()
			currentList[2].append(topDisk3)

		if topDisk2 == -1 or topDisk3 < topDisk2:
			currentList[2].pop()
			currentList[1].append(topDisk3)
			value = (tuple(currentList[0]), tuple(currentList[1]), tuple(currentList[2]))

			if value not in explored.keys():
				newState = [x[:] for x in currentList]
				listNewState.append(State(newState, state))
				explored[value] = True

			currentList[1].pop()
			currentList[2].append(topDisk3)

	return listNewState


def BFS(startState):
	global goal

	frontier = deque()
	frontier.append(startState)
	explored = {}
	value = (tuple(startState.listState[0]), tuple(startState.listState[1]), tuple(startState.listState[2]))
	explored[value] = True

	while frontier:
		state = frontier.popleft()

		if state.listState[2] == goal[2]:
			return state

		for stateNeighbour in GetNeighbourState(state, explored):
			frontier.append(stateNeighbour)


stateResult = BFS(startState)
temp = stateResult
result = []

while temp:
	result.append(temp)
	temp = temp.parent

for i in reversed(result):
	i.Print()