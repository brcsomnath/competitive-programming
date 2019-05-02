'''
651. 4 Keys Keyboard


Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.
Key 2: (Ctrl-A): Select the whole screen.
Key 3: (Ctrl-C): Copy selection to buffer.
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out
the maximum numbers of 'A' you can print on screen.
'''

def main():
    N = int(input())

    dp = [0] * N
    support = [0] * N

    for i in range(min(N, 5)):
        dp[i] = i + 1

    for i in range(5, N):
        copy = 2 * dp[i-3]
        next = dp[i-1] + 1

        support[i] = support[i-1]
        if copy >= next and copy >= (dp[i-1] + support[i-1]) and copy >= (dp[i-2] + support[i-2]):
            support[i] = copy // 2
            dp[i] = copy
            continue

        dp[i] = max(next, max(dp[i-1] + support[i-1], dp[i-2] + support[i-2]))
    print(dp[N-1])

if __name__ == "__main__":
    main()