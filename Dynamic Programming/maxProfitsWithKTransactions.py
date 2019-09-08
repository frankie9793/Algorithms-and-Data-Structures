### Time O(nk) | Space O(nk) where n is no of elements in prices array

def maxProfitsWithKTransactions(prices, k):
    if len(prices) == 0:
        return 0
    profits = [[0 for d in prices] for t in range(k + 1)]
    for t in range(1, k + 1):
        maxThusFar = float("-inf")
        for d in range(1, len(prices)):
            maxThusFar = max(maxThusFar, profits[t - 1][d - 1] - prices[d - 1])
            profits[t][d] = max(profits[t - 1][d - 1], prices[d] + maxThusFar)
    return profits[-1][-1]

### Time O(nk) | Space O(n)

def maxProfitsWithKTransactions(prices, k):
    if len(prices) == 0:
        return 0
    evenProfits = [0 for d in prices]
    oddProfits = [0 for d in prices]
    for t in range(1, k + 1):
        maxThusFar = float("-inf")
        if t % 2 == 0:
            currentProfits = evenProfits
            prevProfits = oddProfits
        else:
            currentProfits = oddProfits
            prevProfits = evenProfits
        for d in range(1, len(prices)):
            maxThusFar = max(maxThusFar, prevProfits[d - 1] - prices[d - 1])
            currentProfits[d] = max(currentProfits[d - 1], maxThusFar + prices[d])
    return evenProfits[-1] if t % 2 == 0 else oddProfits[-1] 
