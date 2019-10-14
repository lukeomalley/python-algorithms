class MinHeap:
  def __init__(self, array):
    self.heap = self.buildHeap(array)

  def swap(self, i, j, heap):
    heap[i], heap[j] = heap[j], heap[i]

  # O(n) TIME | O(1) SPACE
  def buildHeap(self, array):
    firstParentIdx = (len(array) - 2) // 2
    for currentIdx in reversed(range(firstParentIdx)):
      self.siftDown(currentIdx, len(array) - 1, array)
    return array

  # O(log(n)) TIME | O(1) SPACE
  def siftDown(self, currentIdx, endIdx, heap):
    childOneIdx = (currentIdx * 2) + 1
    while childOneIdx <= endIdx:
      childTwoIdx = (currentIdx * 2) + 2 if (currentIdx * 2) + 2 <= endIdx else -1
      if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
        indexToSwap = childTwoIdx
      else:
        indexToSwap = childOneIdx
      if heap[indexToSwap] < heap[currentIdx]:
        self.swap(currentIdx, indexToSwap, heap)
        currentIdx = indexToSwap
        childOneIdx = (currentIdx * 2) + 1
      else:
        break


  # O(log(n)) TIME | O(1) SPACE
  def siftUp(self, currentIdx, heap):
    # get parent index
    parentIdx = (currentIdx - 1) // 2
    while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
      self.swap(currentIdx, parentIdx, heap)
      currentIdx = parentIdx
      parentIdx = (currentIdx - 1) // 2


  # O(log(n)) TIME | O(1) SPACE
  def peak(self):
    return self.heap[0]
  
  # O(log(n)) TIME | O(1) SPACE
  def remove(self):
    self.swap(0, len(self.heap) - 1, self.heap)
    valueToRemove = self.heap.pop()
    self.siftDown(0, (len(self.heap) - 1), self.heap)
    return valueToRemove

  # O(log(n)) TIME | O(1) SPACE
  def insert(self, value):
    self.heap.append(value)
    self.siftUp(len(self.heap) - 1, self.heap)


minHeap = MinHeap([45, 23, 32, 23, 75, 23, 76, 23, 12, 432, 3, 2, 34, 45])