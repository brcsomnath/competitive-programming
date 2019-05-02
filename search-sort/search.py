
def bin_search(arr, left, right, x):

    if right >= left:
        mid = int((left + right)/2)

        if arr[mid] == x:
            return mid
        
        if arr[mid] > x:
            return bin_search(arr, left, mid-1, x)
        
        if arr[mid] < x:
            return bin_search(arr, mid + 1, right, x)
    
    return -1

def bin_search_rotated(arr, left, right, x):
    mid = int((left + right)/2)

    if left > right:
        return -1

    if arr[mid] == x:
        return mid
    
    if arr[left] <= arr[mid]:
        if x >= arr[left] and x <= arr[mid]:
            return bin_search_rotated(arr, left, mid-1, x)
        return bin_search_rotated(arr, mid+1, right, x)
    
    if x >= arr[mid] and x <= arr[right]:
        return bin_search_rotated(arr, mid+1, right, x)
    return bin_search_rotated(arr, left, mid-1, x)

def main():
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3] 
    # arr.sort()
    print(bin_search_rotated(arr, 0, len(arr)-1, 10))

if __name__ == '__main__':
    main()