def invertBinaryTree(tree):
  queue = [tree]
  while len(queue):
    current = queue.pop(0)
    if current is None:
      continue
    swapLeftAndRight(current)
    queue.append(current.left)
    queue.append(current.right)

def swapLeftAndRight(tree):
  tree.right, tree.left = tree.left, tree.right