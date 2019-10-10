# You are given a two-dimensional array (matrix) of potentially unequal height and width containing only 0s and 1s. Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determine its size. Write a function that returns an array of the sizes of all rivers represented in the input matrix. Note that these sizes do not need to be in any particular order.

# O(wh) TIME | O(wh) SPACE
def riverSizes(matrix):
  sizes = []
  visited = [[False for value in row] for row in matrix]
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if visited[i][j]:
        continue
      traverseNode(i, j, matrix, visited, sizes)
  return sizes


def traverseNode(i, j, matrix, visited, sizes):
  currentRiverSize = 0
  # Apply DFS
  # BFS would use a queue instead of a stach
  nodesToExplore = [[i, j]] # Treat this as a stack push all neightbor nodes into this 
  while len(nodesToExplore):
    currentNode = nodesToExplore.pop()
    i = currentNode[0]
    j = currentNode[1]
    if visited[i][j]:
      continue
    visited[i][j] = True
    
    if matrix[i][j] == 0:
      continue

    # If we get here we know that we are dealing with a river that we have not seen yey
    currentRiverSize += 1

    # Get our unvisited neighbors and push them onto the stack
    unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
    for neighbor in unvisitedNeighbors:
      nodesToExplore.append(neighbor)
  if currentRiverSize > 0:
    sizes.append(currentRiverSize)

def getUnvisitedNeighbors(i, j, matrix, visited):
  unvisitedNeighbors = []
  # check that the four neighbors are potentially valid neighbors
  if i > 0 and not visited[i - 1][j]:
    unvisitedNeighbors.append([i - 1, ])
  if i < len(matrix) - 1 and not visited[i + 1][j]:
    unvisitedNeighbors.append([i + 1, j])
  if j > 0 and not visited[i][j - 1]:
    unvisitedNeighbors.append([i, j - 1])
  if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
    unvisitedNeighbors.append([i, j + 1])
  return unvisitedNeighbors

# TEST
result = riverSizes(
  [[1, 0, 0, 1, 0],
   [1, 0, 1, 0, 0],
   [0, 0, 1, 0, 1],
   [1, 0, 1, 0, 1],
   [1, 0, 1, 1, 0]
  ])

print(result)
print(result == [1, 2, 2, 2, 5])