class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def __str__(self):
    result = ''
    result += str(self.value)
    result += ' '
    if self.left:
      result += str(self.left)
    if self.right:
      result += str(self.right)
      result += ' '
    return result

  # Average O(log(n)) time | O(1) space
  # Worst O(n) time | O(1) space
  def insert(self, value):
    curr = self
    while True:
      if value < curr.value:
        if curr.left is None:
          curr.left = BST(value)
          break
        else:
          curr = curr.left
      else:
        if curr.right is None:
          curr.right = BST(value)
          break
        else:
          curr = curr.right
    return self
  
  # Average O(log(n)) time | O(1) space
  # Worst O(n) time | O(1) space
  def contains(self, value):
    curr = self
    while curr is not None:
      if value < curr.value:
        curr = curr.left
      elif value > curr.value:
        curr = curr.right
      else:
        return True
    return False

  def minimum(self):
    curr = self
    while True:
      if curr.left is None:
        return curr.value
      else:
        curr = curr.left
    return self

  def maximum(self):
    curr = self
    while True:
      if curr.right is None:
        return curr.value
      else:
        curr = curr.right
    return self

  # Average O(log(n)) time | O(1) space
  # Worst O(n) time | O(1) space
  def remove(self, value, parent = None):
    curr = self
    while curr is not None:
      if value < curr.value:
        parent = curr
        curr = curr.left
      elif value > curr.value:
        parent = curr
        curr = curr.right
      else:
        # here we have found the value that we want to delete
        if curr.right is not None and curr.left is not None:
          curr.value = curr.right.minimum()
          curr.right.remove(curr.value, curr)
        elif parent is None:
          if curr.left is not None:
            curr.value = curr.left.value
            curr.right = curr.left.right
            curr.left = curr.left.left
          elif curr.right is not None:
            curr.value = curr.right.value
            curr.left = curr.right.left
            curr.right = curr.right.right
          else:
            curr.value = None
        elif parent.left is curr:
          parent.left = curr.left if curr.left is not None else curr.right
        elif parent.right is curr:
          parent.right = curr.left if curr.left is not None else curr.right
        break
    return self

root = BST(10)

root.insert(4)
root.insert(3)
root.insert(7)
root.insert(12)
root.insert(15)
root.insert(20)

print(root.__str__())
root.remove(10)
print(root.__str__())
print('minimum:', root.minimum())
print('maximum:', root.maximum())
print(root.contains(20))


