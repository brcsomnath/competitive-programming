'''
3Sum Smaller

Given an array of n integers nums and a target,
find the number of index triplets i, j, k with 0 <= i < j < k < n 
that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.
Return 2. Because there are two triplets which sums are less than 2:
'''

def twoSumSmaller(arr, target):
    sum = 0
    start, end = 0, len(arr) - 1
    while start < end:
        if arr[start] + arr[end] >= target:
            end -= 1
        else:
            sum += (end - start)
            start += 1
    return sum

def process(arr, target):
    arr = sorted(arr)

    ans = 0
    for i in range(len(arr)):
        ans += twoSumSmaller(arr[i+1:], target - arr[i])
    return ans

def main():
    array = [int(x) for x in input().split()]
    target = int(input())

    print(process(array, target))

if __name__ == "__main__":
    main()