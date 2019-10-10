# O(n) TIME | O(1) SPACE
def kadanesAlgorithm(array):
  maxSoFar = array[0]
  maxEndingHere = array[0]
  for i in range(1, len(array)):
    maxEndingHere = max(maxEndingHere + array[i], array[i]) 
    maxSoFar = max(maxSoFar, maxEndingHere)
  return maxSoFar 

print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
