'''
471. Encode String with Shortest Length

Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

Note:

k will be a positive integer and encoded string will not be empty or have extra space.
You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.
Example 1:
Input: "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.

Example 2:

Input: "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.

Example 3:

Input: "aaaaaaaaaa"
Output: "10[a]"
'''

def solve():
    word = input()

    dp = [["" for i in range(N)] for j in range(N)]
    for L in range(N):
        for start in range(N-L):
            end = start + L + 1
            substr = word[start:end]

            if end - start < 5:
                dp[start][end] = substr
            else:
                dp[start][end] = substr
                for k in range(start, end-1):
                    if len(dp[start][k] + dp[k+1][end]) < len(dp[start][end]):
                        dp[start][end] = dp[start][k] + dp[k+1][end]

                for k in range(len(substr)):
                    pattern = substr[: k + 1]
                    if len(substr) % len(pattern) == 0 and len(substr.replace(pattern, "")) == 0:
                        ans = str(len(substr)//len(pattern)) + "[" + pattern + "]"
                        if len(ans) < len(dp[start][end]):
                            dp[start][end] = ans
    return dp[0][len(word) - 1]




if __name__ == "__main__":
    solve()