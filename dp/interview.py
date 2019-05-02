
def check_palindrome(word):
    start, end = 0, len(word)-1

    while start < end:
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

def check_possible(x, y):
    n = len(x)
    for first_cut in range(n):
        for second_cut in range(n):
            if not check_palindrome(x[0:first_cut] + y[second_cut:n])
                return False
    return True

def main():
    x, y = input().split()
    print(check_palindrome(x))

if __name__ == "__main__":
    main()