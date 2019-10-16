# Upper bound O(n^2 * n!) TIME | O(n * n!) SPACE
def getPermutations(array):
  permutations = []
  permutationsHelper(array, [], permutations)
  return permutations

def permutationsHelper(array, currentPermutation, permutations):
  if not len(array) and len(currentPermutation):
    permutations.append(currentPermutation)
  else:
    for i in range(len(array)):
      newArray = array[:i] + array[i + 1:]
      newPermutation = currentPermutation + [array[i]]
      permutationsHelper(newArray, newPermutation, permutations)

print(getPermutations([1, 2, 3]))


# O(n * n!) TIME | O(n * n!) SPACE
def getPermutationsImproved(array):
  permutations = []
  permutationsHelperImproved(0, array, permutations)
  return permutations

def permutationsHelperImproved(i, array, permutations):
  if i == len(array) - 1:
    permutations.append(array[:])
  else:
    for j in range(i, len(array)):
      swap(array, i, j)
      permutationsHelperImproved(i + 1, array, permutations)
      swap(array, i, j)

def swap(array, i, j):
  array[i], array[j] = array[j], array[i]

print(getPermutationsImproved([1, 2, 3]))