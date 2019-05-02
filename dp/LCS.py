
def lcs(x, y):
    m, n = len(x), len(y)
    dp = [[0]*(n+1)]*(m + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


def lcs_inp():
    with open('input') as fp:
        for line in fp:
            X, Y = line.strip().split()
            print(lcs(X, Y))

if __name__ == "__main__":
    main()