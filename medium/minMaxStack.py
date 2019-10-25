class MinMaxStack:
  def __init__(self):
    self.minMaxStack = []
    self.stack = []

  # O(1) TIME | O(1) SPACE
  def peek(self):
    return self.stack[len(self.stack) - 1]

  # O(1) TIME | O(1) SPACE
  def pop(self):
    self.minMaxStack.pop()
    return self.stack.pop()

  # O(1) TIME | O(1) SPACE
  def push(self, number):
    newMinMax = {"min": number, "max": number}
    if len(self.minMaxStack):
      lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
      newMinMax["min"] = min(lastMinMax["min"], number)
      newMinMax["max"] = max(lastMinMax["max"], number)
    self.minMaxStack.append(newMinMax)
    self.stack.append(number)
    return self

  # O(1) TIME | O(1) SPACE
  def getMin(self):
    return self.minMaxStack[len(self.minMaxStack) - 1]["min"]
  
  # O(1) TIME | O(1) SPACE
  def getMax(self):
    return self.minMaxStack[len(self.minMaxStack) - 1]["max"]