'''
Given two strings S and T, find length of the shortest subsequence in S 
which is not a subsequence in T. If no such subsequence is possible, return -1.
A subsequence is a sequence that appears in the same relative order,
 but not necessarily contiguous. A string of length n has  2^n different possible subsequences.

String S of length m (1 <= m <= 1000)
String T of length n (1 <= n <= 1000)
'''

def shortest_seq(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n+1)] * (m+1)

    for j in range(n+1):
        dp[0][j] = 1005

    for i in range(m+1):
        dp[i][0] = 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            for k in range(j-1, 0, -1):
                if S[i-1] == T[k]:
                    break
            
            if k == -1:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][k] + 1)
    
    ans = dp[m][n]
    return ans if ans < 1005 else -1

def main():
    S, T = input().split()
    print(shortest_seq(S, T))

if __name__ == "__main__":
    main()
