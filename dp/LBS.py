'''
Longest Bitonic Subsequence | DP-15
Given an array arr[0 … n-1] containing n positive integers, a subsequence of arr[] is 
called Bitonic if it is first increasing, then decreasing. Write a function that takes 
an array as argument and returns the length of the longest bitonic subsequence.
A sequence, sorted in increasing order is considered Bitonic with the decreasing part as empty. 
Similarly, decreasing order sequence is considered Bitonic with the increasing part as empty.

Examples:

Input arr[] = {1, 11, 2, 10, 4, 5, 2, 1};
Output: 6 (A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1)

Input arr[] = {12, 11, 40, 5, 3, 1}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 12, 11, 5, 3, 1)

Input arr[] = {80, 60, 30, 40, 20, 10}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 80, 60, 30, 20, 10)
'''

def LBS(arr):
    N = len(arr)
    dp = [1] * N

    reversed_arr = arr[::-1]
    inv_dp = [1] * N
    max_bitonic = 0

    for i in range(1, N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        
    

    for i in range(1, N):
        for j in range(j):
            if reversed_arr[i] > reversed_arr[j]:
                inv_dp[i] = max(inv_dp[i], inv_dp[j] + 1)

        max_bitonic = max(max_bitonic, dp[i] + inv_dp[i] - 1)
    return max_bitonic

