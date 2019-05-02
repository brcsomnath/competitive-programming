'''
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    N = len(s)
    dp = [False for i in range(N)]
    
    for i in range(N):
        if not dp[i] and s[:i+1] in wordDict:
            dp[i] = True
        
        if dp[i]:
            for j in range(i+1, N):
                if not dp[j] and s[i+1:j+1] in wordDict:
                    dp[j] = True
    return dp[N-1]
        