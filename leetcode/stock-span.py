
def calculate_span(arr):
    stack = []
    ans = [0]*len(arr)
    stack.append(0)
    ans[0] = 1

    for i in range(1, len(arr)):
        while len(stack) > 0 and arr[i] > arr[stack[-1]]:
            stack.pop()

        ans[i] = (i + 1) if len(stack) == 0 else (i - stack[-1])
        stack.append(i)
    return ans

def get_span(arr):
    ans = [0] * len(arr)
    ans[0] = 1

    for i in range(1, len(arr)):
        counter = 1
        while (i - counter) >= 0 and arr[i] > arr[i - counter]:
            counter += ans[i - counter]
        ans[i] = counter
    return ans


def main():
    with open('input') as file:
        for line in file:
            arr = [int(n) for n in list(line.split(', '))]
            print(calculate_span(arr))

if __name__ == "__main__":
    main()