# Write a function that takes in an array of unique integers and returns its powerset. 
# The powerset P(X) of a set X is the set of all subsets of X. 
# For example, the powerset of [1,2] is [[], [1], [2], [1,2]]. 
# Note that the sets in the powerset do not need to be in any particular order.

# O(2^n*n) TIME | O(2^n*n) SPACE
def powerset(array):
  subsets = [[]]

  for element in array:
    for i in range(len(subsets)):
      currentSubset = subsets[i]
      subsets.append(currentSubset + element)

  return subsets
