'''
Given two strings of lower alphabet characters, we need to find the number of ways to insert 
a character in the first string such that length of LCS of both strings increases by one.

Examples:

Input : str1 = “abab”, str2 = “abc”
Output : 3
LCS length of given two strings is 2.
There are 3 ways of insertion in str1, 
to increase the LCS length by one which 
are enumerated below, 
str1 = “abcab”	str2 = “abc”  LCS length = 3
str1 = “abacb”	str2 = “abc”  LCS length = 3
str1 = “ababc”	str2 = “abc”  LCS length = 3

Input : str1 = “abcabc”, str2 = “abcd”
Output : 4
'''


from collections import defaultdict

def ways_to_increase(word1, word2):

    front = [[0] * (len(word2) + 1)] * (len(word1) + 1)
    back = [[0] * (len(word2) + 2)] * (len(word1) + 2)

    char_store = defaultdict(list)
    for i in range(len(word2)):
        char_store[word2[i]].append(i)

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i-1] == word2[j-1]
                front[i][j] = front[i-1][j-1] + 1
            else:
                front[i][j] = max(front[i-1][j], front[i][j-1])

    for i in range(len(word1) + 1, 0, -1):
        for j in range(len(word2) + 1, 0, -1):
            if word1[i-1] == word2[j-1]
                back[i][j] = back[i+1][j+1] + 1
            else:
                back[i][j] = max(back[i+1][j], back[i][j+1])

    ways = 0
    for i in range(1, len(word1) + 1):
        for j in range(26):
            ch = chr(97 + j)

            for pos in range(len(char_store[ch])):
                if front[i][pos-1] +  back[N-i-1][pos+1] == front[len(word1)][len(word2)]:
                    ways += 1

    return ways

    

    