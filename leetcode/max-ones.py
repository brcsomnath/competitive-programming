'''
487. Max Consecutive Ones II

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream?
 In other words, you can't store all numbers coming from the stream as it's too
  large to hold in memory. Could you solve it efficiently?
'''

def main():
    arr = [int(x) for x in input().split()]
    l, zeros = 0, 0
    count = 0

    for idx in len(arr):
       if arr[idx] == 0:
           zeros += 1
        
        while zeros > 1:
            l += 1
            if arr[l] == 0:
                zeros -= 1
        count = max(count, idx - l + 1)

    return count

if __name__ == "__main__":
    main()