# Write a function that takes in a 'special' array and returns its product sum. 
# A 'special' array is a non-empty array that contains either intergers of other 'special'
# arrays. The product sum of a 'spceial' array is the sum of its elements, where 'scpeial'
# arrays inside it should be summed themselves and then multiplied by there level of depth
# For example, the product sum of [x, y] is x + y. The product sum of [x, [y, z]] is x + 2y + 2z

def productSum(array, multiplier = 1):
  sum = 0
  for element in array:
    if type(element) is list: 
      sum += productSum(element, multiplier + 1)
    else:
      sum += element
  return sum * multiplier

print(productSum([5, 2, [7, 1], 3, [6, [-13, 8], 4]]))