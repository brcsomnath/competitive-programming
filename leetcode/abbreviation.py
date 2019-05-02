'''

Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

'''

def process(word):
    length = len(word)
    ans = []

    for x in range(2**length):
        candidate, count = "", 0
        for i in range(length):
            if x & (1<<i):
                if count != 0:
                    candidate += str(count)
                candidate += word[i]
                count = 0
            else:
                count += 1
        if count > 0:
            candidate += str(count)
        ans.append(candidate)
    return ans

def main()
    word = input()

if __name__ == "__main__":
    main()