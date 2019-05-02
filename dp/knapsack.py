
def knapsack(weights, values, W):
    dp = [0] * (len(weights) + 1)

    for i in range(len(weights)):
        for j in range(W, weights[i]-1, -1):
            dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
    return dp[len(weights)]