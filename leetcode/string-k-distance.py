'''
Rearrange String k Distance Apart

Given a non-empty string s and an integer k, rearrange the string such
 that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange
 the string, return an empty string "".
'''

from collections import defaultdict
from queue import deque

def main():
    str = input()
    k = int(input())

    char_map = defaultdict(lambda: 0)
    for c in str:
        char_map[c] += 1
    
    q = deque()
    for k in char_map.keys():
        q.append(k)
    
    length = len(str)
    ans = ""
    while len(q) > 0:
        cnt = min(k, length)
        temp = []
        for i in range(cnt):
            ch = q.popleft()
            ans += ch
            char_map[ch] -= 1
            if char_map[ch] > 0:
                temp.append(ch)
        
        for c in temp:
            q.append(c)


if __name__ == "__main__":
    main()