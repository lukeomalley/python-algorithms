# Given an array of positive integers representing coin denominations and a single non-negative integer representing a target amount of money, implement a function that returns the smallest number of coins needed to make change for that target amount using the given coin denominations. Note that an unlimited amount of coins is at your disposal. If it is impossible to make change for the target amount, return -1.
# Sample input: 7, [1, 5, 10]
# Sample output: 3 (2x1 + 1x5)
def minNumberOfCoinsForChange(n, denoms):
  minNumOfCoins = [float("inf") for num in range(n + 1)]
  minNumOfCoins[0] = 0
  for denom in denoms:
    for amount in range(len(minNumOfCoins)):
      if denom <= amount:
        minNumOfCoins[amount] = min(minNumOfCoins[amount], 1 + minNumOfCoins[amount - denom])
  return minNumOfCoins[n] if minNumOfCoins[n] != float("inf") else -1

minNumberOfCoinsForChange(10, [1, 5, 10])

print(minNumberOfCoinsForChange(7, [1, 5, 10]) == 3)