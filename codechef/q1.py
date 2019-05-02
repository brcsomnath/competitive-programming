from bisect import bisect_left

def main():
    N = int(input())
    arr = [int(x) for x in input().split()]

    max_mod = 0

    arr.sort()
    for i in range(N-1, -1, -1):
        if max_mod >= arr[i]:
            break
        
        if i>0 and arr[i] == arr[i-1]:
            continue
        
        for num in range(arr[i], arr[N-1] + arr[i], arr[i]):
            idx = bisect_left(arr, num)
            max_mod = max(max_mod, arr[idx - 1]% arr[i])
    print(max_mod)

if __name__ == "__main__":
    main()