# O(nd) Time | O(n) Space where n is target 
def minNumberOfCoinsForChange(target, denoms):
    numOfCoins = [float("inf") for amount in range(target + 1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], 1 + min(numOfCoins[amount - denom]))
    return numOfCoins[target] if numOfCoins[target] != float("inf") else -1