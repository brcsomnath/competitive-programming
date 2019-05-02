'''
Partition problem | DP-18
Partition problem is to determine whether a given set can be partitioned into two subsets such 
that the sum of elements in both subsets is same.
Examples:

arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.
'''

def check_partition(arr):
    total = sum(arr)

    dp = [[False]*(len(arr) + 1)]*(total//2 + 1)
    for i in range(len(dp[0])):
        dp[0][i] = True
    
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j] = dp[i][j-1]
            if i >= arr[j]:
                dp[i][j] = dp[i][j] | dp[i-arr[j]][j]
    return dp[total//2][len(arr)]
