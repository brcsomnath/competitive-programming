
def get_pivot(arr):
    pivot = arr[-1]

    idx = -1
    for i in range(len(arr)-1):
        if arr[i] <= pivot:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]

    arr[idx + 1], arr[len(arr)-1] = arr[len(arr)-1], arr[idx + 1]
    return idx + 1

def find_nth_smallest(arr, N):

    N -= 1
    while len(arr) > 0:
        p = get_pivot(arr)
        if p == N:
            return arr[N]

        if p > N:
            N = N - p
            arr = arr[p+1:]
        else:
            arr = arr[:p+1]


    

