import sys

def min_cuts(word):
    N = len(word)
    dp = [[False] * N] * N

    for i in range(N):
        dp[i][i] = True # single letter always a palindrome

    for L in range(2, N):
        for start in range(N-L):
            end = start + L
            if L == 2:
                dp[start][end] = True if word[start] == word[end] else False
                continue
            dp[start][end] = word[start] == word[end] and dp[start + 1][end - 1]
    

    cost = [float('inf')] * N # to calculate the cost

    for end in range(N):
        if dp[0][end]: # if the string[:i] is palindrome no cuts
            cost[end] = 0
        else:
            for start in range(end): # check for minimum by dividing into palindromes
                if dp[start+1][end]:
                    cost[end] = min(cost[start] + 1, cost[end])

    return cost[N-1] # cost at the end

            
