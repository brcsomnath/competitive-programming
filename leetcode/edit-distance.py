'''
One Edit Distance

Given two strings S and T, determine if they are both one edit distance apart.
'''

def edit_distance(word1, word2):
    dp = [[0]*(len(word1) + 1)]*(len(word2) + 1)

    for i in range(len(word1)+1):
        dp[i][0] = i
    
    for j in range(len(word2)+1):
        dp[0][j] = j

    for i in range(1, len(word1)):
        for j in range(1, len(word2)):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[len(word1)-1][len(word2)-1] == 1

def one_edit_distance(word1, word2):
    M, N = len(word1), len(word2)

    if abs(M - N) > 1: return False
    
    dist = 0
    i, j = 0,  0

    while i < M and j < N:
        if word1[i] != word2[j]:
            if dist == 1:
                return False
            
            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:
                i += 1
                j += 1
            dist += 1
        else:
            i += 1
            j += 1

    return dist == 1
        

def main():
    str1, str2 = input()
    print(one_edit_distance(str1, str2))

if __name__ == "__main__":
    main()