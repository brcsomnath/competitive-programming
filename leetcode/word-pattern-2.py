'''
291. Word Pattern II

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.
Notes:
You may assume both pattern and str contains only lowercase letters.
'''

def process(word, pattern):
    W, P = len(word), len(pattern)
    if W % P != 0:
        return False
    
    block_size = len(word) // len(pattern)
    mp = dict()

    for i in range(len(pattern)):
        if pattern[i] not in mp.keys():
            mp[pattern[i]] = word[i*block_size : (i+1)*block_size]
            continue
        
        if mp[pattern[i]] != word[i*block_size : (i+1)*block_size]:
            return False
    return True

def main():
    string, pattern = input().split()

if __name__ == "__main__":
    main()