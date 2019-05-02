'''
Maximum Average Subarray II

Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
'''
import sys

def process(arr, k):
    minimum, maximum = 10001, -10001

    for num in arr:
        minimum = min(minimum, num)
        maximum = max(maximum, num)

    prev_mid, error = maximum, maximum

    while error > 0.00001:
        mid = (minimum + maximum)/2

        if bin_search(arr, mid):
            minimum = mid
        else:
            maximum = mid
        error = abs(prev_mid - mid)
        prev_mid = mid
    return minimum

def bin_search(arr, target):
    curr, prev = 0, 0

    for i in range(k):
        curr += (arr[i] - target)
    
    if curr >= 0:
        return True
    
    min_sum = sys.maxsize
    for i in range(k, len(arr)):
        curr += (arr[i] - target)
        prev += arr[i-k]
        min_sum = min(min_sum, prev)
        if curr >= min_sum:
            return True
    return False


def main():
    array = [int(element) for element in input().split()]
    k = int(input())


if __name__ == "__main__":
    main()