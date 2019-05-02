
def partition(arr, left, right):
    pivot = arr[right - 1]
    i = left-1 # smaller element

    for j in range(left, right-1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[right-1] = arr[right-1], arr[i+1]
    return (i+1)


def quick_sort(arr, start, end):

    if start < end:
        pi = partition(arr, start, end)

        quick_sort(arr, start, pi-1)
        quick_sort(arr, pi+1, end)

def quick_select(arr, start, end, position):
    if start < end:
        pi = partition(arr, start, end)

        if pi == position-1:
            return arr[position]
        
        if position-1 < pi:
            return quick_select(arr, start, pi-1, position)
        return quick_select(arr, pi+1, end, position - pi + start - 1)

def main():
    arr = [7, 10, 4, 3, 20, 15]
    print(quick_select(arr, 0, len(arr), 4))
    quick_sort(arr, 0, len(arr))
    print(arr)

if __name__ == '__main__':
    main()