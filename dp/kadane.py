

def max_contiguous_sum(arr):
    sum, max_sum = 0, -1*float('inf')
    start, end = -1, -1

    local_start = 0
    for i in range(len(arr)):
        sum += arr[i]

        if sum < 0:
            sum = 0
            local_start = i + 1
        else:
            max_sum = max(max_sum, sum)
            start = local_start
            end = i

    return max_sum, [start, end]