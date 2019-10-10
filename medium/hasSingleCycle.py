def hasSingleCycle(array):
  for i in range(0, len(array)):
    visitedNodes = {}
    idx = i
    visitedNodes[idx] = True
    while len(visitedNodes) <= len(array):
      idx += array[idx]
      if idx > len(array):
        idx = idx % len(array) + 1
      elif idx < 0:
        idx = len(array) - abs(idx % len(array))
      if idx in visitedNodes:
        break
      else:
        visitedNodes[idx] = True
    return True
  return False
     

print(hasSingleCycle([2, 3, 1, -4, -4, 2]))

def hasSingleCycleImproved(array):
  numElementsVisited = 0
  currentIdx = 0
  while numElementsVisited < len(array):
    if numElementsVisited > 0 and currentIdx == 0:
      return False
    numElementsVisited += 1
    currentIdx = getNextIdx(currentIdx, array)
  return currentIdx == 0

def getNextIdx(currentIdx, array):
  jump = array[currentIdx]
  nextIdx = (currentIdx + jump) % len(array)
  return nextIdx if nextIdx >= 0 else nextIdx + len(array)

print(hasSingleCycleImproved([2, 3, 1, -4, -4, 2]))