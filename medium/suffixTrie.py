class SuffixTrie: 
  def __init__(self, string):
    self.root = {}
    self.endSymbol = '*'
    self.populateSuffixTrieFrom(string)

  # O(n^2) TIME | O(n^2) SPACE
  def populateSuffixTrieFrom(self, string):
    for i in range(len(string)):
      self.insertSubstringStringStartingAt(i, string)
    return None

  def insertSubstringStringStartingAt(self, index, string):
    node = self.root
    for j in range(index, len(string)):
      currentLetter = string[j]
      if currentLetter not in node:
        node[currentLetter] = {}
      node = node[currentLetter]
    node[self.endSymbol] = True
    return None

  # O(m) TIME | O(1) SPACE
  def contains(self, string):
    node = self.root
    for letter in string:
      if letter not in node:
        return False
      node = node[letter]
    return self.endSymbol in node
