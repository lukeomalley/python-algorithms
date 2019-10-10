import math

def smallestDifference(arrayOne, arrayTwo):
  result = []
  smallest = math.inf
  for x in arrayOne:
    for y in arrayTwo:
      if abs(x - y) < smallest:
        smallest = abs(x - y)
        result = [x, y]
  return result

        
    
def smallestDifferenceImproved(arrayOne, arrayTwo):
  arrayOne.sort()
  arrayTwo.sort()
  print(arrayOne)
  print(arrayTwo)
  smallest = math.inf
  result = []
  i = 0
  j = 0

  while i < len(arrayOne) and j < len(arrayTwo):
    if arrayOne[i] < arrayTwo[j]:
      if abs(arrayOne[i] - arrayTwo[j]) < smallest:
        smallest = abs(arrayOne[i] - arrayTwo[j])  
        result = [arrayOne[i], arrayTwo[j]]
      i += 1
    else:
      if abs(arrayOne[i] - arrayTwo[j]) < smallest:
        smallest = abs(arrayOne[i] - arrayTwo[j])
        result = [arrayOne[i], arrayTwo[j]]
      j += 1
  return result
    
print(smallestDifferenceImproved([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

      
    