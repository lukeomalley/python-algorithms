# You are given a two-dimensional array (matrix) of distinct integers 
# where each row is sorted and each column is also sorted. 
# The matrix does not necessarily have the same height and width. 
# You are also given a target number, and you must write a function that 
# returns an array of the row and column indices of the target number if it is 
# contained in the matrix and [-1, -1] if it is not contained in the matrix.

# O(n + m) TIME | O(1) SPACE
def searchInSortedMatrix(matrix, target):
  row = 0
  col = len(matrix[0]) - 1

  while row < len(matrix) and col >= 0:
    if matrix[row][col] > target:
      col -= 1
    elif matrix[row][col] < target:
      row += 1
    else:
      return [row, col]

  return [-1, -1]