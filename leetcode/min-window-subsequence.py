'''
727. Minimum Window Subsequence

Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:
Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
'''

def LCS(S, T):
    N, M = len(S), len(T)

    # dp[i][j] = start position of the subsequence T[:j] 
    # contained in S[:i]
    dp = [[-1 for i in range(M+1)] for j in range(N+1)]

    for i in range(N+1):
        dp[i][0] = i

    min_len = float('inf')
    start = -1
    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = dp[i-1][j-1] if S[i-1] == T[j-1] else dp[i-1][j]

            if dp[i][N] != -1:
                if (i - dp[i][N]) < min_len:
                    min_len = (i - dp[i][N])
                    start = dp[i][N]
    return S[start : start + min_len + 1] if start != -1 else -1

    

