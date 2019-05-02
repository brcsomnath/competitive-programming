''' 
* Google 
* Given a list of non-negative numbers and a target integer k, 
* write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer. 
'''

def validate(arr, k):
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]

    for last in range(len(arr), 0):
        for first in range(0, len(arr)):
            sum = (arr[last] - arr[first])
            if sum % k == 0 and (last - first) > 0:
                return True
            if arr[first] % k == 0 and first > 0:
                return True
    return False

def main():
    pass

if __name__ == "__main__":
    main()