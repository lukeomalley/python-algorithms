class MinHeap:
  def __init__(self, array):
    self.heap = self.buildHeap(array)

  def buildHeap(self, array):

  def siftDown(self, currentIdx, endIdx, heap):


  def siftUp(self, currentIdx, heap):
    # get parent index
    parentIdx = (currentIdx - 1) // 2
    while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
      self.swap(currentIdx, parentIdx, heap)
      currentIdx = parentIdx
      parentIdx = (currentIdx - 1) // 2


  def peak(self):
    return self.heap[0]
  
  def remove(self):
    swap(0, len(self.heap) - 1, self.heap)
    valueToRemove = self.heap.pop()
    self.siftDown(0, len(self.heap) - 1), self.heap
    return valueToRemove

  def insert(self, value):
    self.heap.append(value)
    self.siftUp(len(self.heap) - 1, self.heap)