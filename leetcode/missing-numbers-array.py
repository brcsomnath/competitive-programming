'''
Find All Numbers Disappeared in an Array
Given an array of integers where 1 < a[i] < n (n = size of array),
 some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned 
list does not count as extra space.
'''

def main():
    arr = list(map(int, input().split()))

    mask = 0
    for n in arr:
        mask |= 1<<n
    
    res = []
    for i in range(1, len(arr)+1):
        if not mask >> i & 1:
            res.append(i)
    return res

if __name__ == "__main__":
    print(main())