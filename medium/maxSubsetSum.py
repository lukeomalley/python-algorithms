# O(n) TIME | O(n) SPACE
def maxSubsetSum(array):
  if not len(array):
    return
  elif len(array) == 1:
    return array[0]

  maxSums = array[:]
  maxSums[1] = max(array[0], array[1])

  for i in range (2, len(array)):
    maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])

  return maxSums[-1]


# O(n) TIME | O(1) SPACE
  def maxSubsetSumsImproved(array):
    if not len(array):
      return 0
    elif len(array) == 1:
      return array[0]
    
    second = array[0]
    first = max(array[0], array[1])

    for i in range(2, len(array)):
      current = max(first, second + array[i])
      second = first
      first = second

    return first