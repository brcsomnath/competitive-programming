'''
Given an unsorted array nums, reorder it in-place
such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4],
one possible answer is [1, 6, 2, 5, 3, 4].
'''

def process(array):
    position = 1

    for index in range(1, len(array)):
        if position & 1:
            if array[index] < array[index - 1]:
                array[index], array[index - 1] = array[index - 1], array[index]
        else:
            if array[index] > array[index - 1]:
                array[index], array[index - 1] = array[index - 1], array[index]
        position = 1 - position
    return array

def main():
    array = [int(element) for element in input().split()]
    print(process(array))

if __name__ == "__main__":
    main()