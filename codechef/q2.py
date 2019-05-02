
def process(word, p, N):
    prev_idx = -1
    ans = 0

    for i in range(N):
        if word[i] == p:
            right = (N - i)
            left = i - prev_idx
            ans += right * left
            prev_idx = i
    print(ans)


def main():
    T = int(input())
    while T > 0:
        N = int(input())
        word, p = input().split()
        process(word, p, N)
        T -= 1

if __name__ == "__main__":
    main()