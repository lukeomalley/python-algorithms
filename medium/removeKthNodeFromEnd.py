# O(n) TIME | O(1) SPACE
def removeKthNodeFromEnd(head, k):
  firstPointer = head
  secondPointer = head
  counter = 1

  while counter <= k:
    secondPointer = secondPointer.next
    counter += 1

  # HERE the secondPointer is k nodes ahead of the firstPointer

  if secondPointer is None:
    # edge case where we need to remove the first node
    head.value = head.next.value
    head.next = head.next.next
    return
  
  # This takes the first pointer to the node before the one we want to remove
  while secondPointer.next is not None:
    firstPointer = firstPointer.next
    secondPointer = secondPointer.next

  firstPointer.next = firstPointer.next.next
