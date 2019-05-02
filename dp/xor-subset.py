'''
Count number of subsets having a particular XOR value
Given an array arr[] of n numbers and a number K, find the number of subsets 
of arr[] having XOR of elements as K

Examples :

Input:   arr[]  = {6, 9, 4,2}, k = 6
Output:  2
The subsets are {4, 2} and {6}

Input:   arr[]  = {1, 2, 3, 4, 5}, k = 4
Output:  4
The subsets are {1, 5}, {4}, {1, 2, 3, 4}
                and {2, 3, 5}
'''
from math import *

def process(arr, k):
    max_element = max(arr)
    N = len(arr)
    M = 1 << ceil(log2(max_element)) - 1 # Max XOR possible

    dp = [[0] for i in range(N+1)] for j in range(M+1)

    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(M+1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j^arr[i]]
    return dp[N][k]



