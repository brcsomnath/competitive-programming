'''
There is a garden with N slots. In each slot, there is a flower. 
The N flowers will bloom one by one in N days. In each day, there will be exactly one
flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array
represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i 
will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists
two flowers in the status of blooming, and also the number of flowers between them
is k and these flowers are not blooming.

If there isn't such day, output -1.
'''

def process(flowers, k):
    days = [0] * len(flowers)
    for i in range(len(flowers)):
        days[flowers[i] - 1] = i + 1
    
    ans = float('inf')

    left, right = 0, k + 1
    while right < len(days):
        for i in range(left+1, right):
            check = 0
            if days[i] < days[left] or days[i] < days[right]:
                left, right = i, i + k + 1
                check = 1
                break
            
            if check == 0:
                ans = min(ans, max(days[left], days[right]))
                left, right = right, right + k + 1
    
    return ans if ans < float('inf') else -1


def main():
    flowers = [int(x) for x in input().split()]
    k = int(input())
    process(flowers, k)
    
if __name__ == "__main__":
    main()