# You're given three inputs, all of which are instances of a class that have an "ancestor" property pointing to their youngest ancestor. The first input is the top ancestor in an ancestral tree (i.e., the only instance that has no ancestor), and the other two inputs are descendants in the ancestral tree. Write a function that returns the youngest common ancestor to the two descendants.
class AncestralTree:
	def __init__(self, name):
		self.name = name
		self.ancestor = None

	def addAsAncestor(self, descendants):
		for descendant in descendants:
			descendant.ancestor = self

# O(d) TIME | O(1) SPACE
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne = getDescendantDepth(descendantOne, topAncestor)
	depthTwo = getDescendantDepth(descendantTwo, topAncestor)

	if depthOne > depthTwo:
		return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
	else:
		return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)

def getDescendantDepth(descendant, topAncestor):
	depth = 0
	while descendant != topAncestor:
		depth += 1
		descendant = descendant.ancestor
	return depth

def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
	while diff > 0:
		lowerDescendant = lowerDescendant.ancestor
		diff -= 1
	while lowerDescendant != higherDescendant:
		lowerDescendant = lowerDescendant.ancestor
		higherDescendant = higherDescendant.ancestor
	return lowerDescendant


























ancestralTrees = {}
ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for letter in ALPHABET:
    ancestralTrees[letter] = AncestralTree(letter)
ancestralTrees['A'].addAsAncestor([
    ancestralTrees['B'],
    ancestralTrees['C'],
    ancestralTrees['D'],
    ancestralTrees['E'],
    ancestralTrees['F'],
])
ancestralTrees['B'].addAsAncestor([
    ancestralTrees['G'],
    ancestralTrees['H'],
    ancestralTrees['I'],
])
ancestralTrees['C'].addAsAncestor([
    ancestralTrees['J'],
])
ancestralTrees['D'].addAsAncestor([
    ancestralTrees['K'],
    ancestralTrees['L'],
])
ancestralTrees['F'].addAsAncestor([
    ancestralTrees['M'],
    ancestralTrees['N'],
])
ancestralTrees['H'].addAsAncestor([
    ancestralTrees['O'],
    ancestralTrees['P'],
    ancestralTrees['Q'],
    ancestralTrees['R'],
])
ancestralTrees['K'].addAsAncestor([
    ancestralTrees['S'],
])
ancestralTrees['P'].addAsAncestor([
    ancestralTrees['T'],
    ancestralTrees['U'],
])
ancestralTrees['R'].addAsAncestor([
    ancestralTrees['V'],
])
ancestralTrees['V'].addAsAncestor([
    ancestralTrees['W'],
    ancestralTrees['X'],
    ancestralTrees['Y'],
])
ancestralTrees['X'].addAsAncestor([
    ancestralTrees['Z'],
])