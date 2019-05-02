# Give you a pattern (digit in the pattern matches the corresponding 
# number of letters, 
# letter means match the letter itself), 
# a string to determine whether match: 
# ex: 
# abc -> 'abc' true 
# '1oc3' -> 'aoczzz', 'bocabc' true

def get_index(character):
    return ord(character) - ord('a')

def match(pattern, word):
    idx = 0
    for p in pattern:
        if get_index(p) >= 0:
            if p != word[idx]:
                return False
        else:
            idx += (int(p) - 1)
            if idx > len(word) - 1:
                return False
        idx += 1
    return True

def main():
    print(match('abc', 'abc'))
    print(match('1oc3', 'aoczzz'))
    print(match('1oc3', 'bocabc'))

if __name__ == "__main__":
    main()