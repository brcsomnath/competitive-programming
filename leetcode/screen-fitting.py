'''
Sentence Screen Fitting

Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
'''

def process(row, col, sentence):

    index, n = 0, len(sentence)
    count = 0

    for i in range(row):
        remain = col
        while remain >= len(sentence[index]):
            remain -= (len(sentence[index]) + 1)
            index = (index + 1)%n
            if index == (n - 1):
                count += 1
    return count

def main():
    row, col = input().split()
    row, col = int(row), int(col)

    sentence = input().split()
    print(process(row, col, sentence))

if __name__ == "__main__":
    main()