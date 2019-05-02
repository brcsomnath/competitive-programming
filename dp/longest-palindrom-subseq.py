'''
Given a sequence, find the length of the longest palindromic subsequence in it.

As another example, if the given sequence is “BBABCBCAB”, then the output should be 7 
as “BABCBAB” is the longest palindromic subseuqnce in it. “BBBBB” and “BBCBB” are also 
palindromic subsequences of the given sequence, but not the longest ones.
'''

def LPS(word):
    N = len(word)
    dp = [[0] * N] * N

    for i in range(N):
        dp[i][i] = 1

    for length in range(1, N):
        for start in range(0, N - length):
            end = start + length

            if word[start] == word[end] and length == 1:
                dp[start][end] = 2
            elif word[start] == word[end]:
                dp[start][end] = dp[start+1][end-1] + 2
            else:
                dp[start][end] = max(dp[start+1][end], dp[start][end-1])

    return dp[0][N-1]