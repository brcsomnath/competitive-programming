'''
Find the longest substring with k unique characters in a given string
Given a string you need to print longest possible substring that has exactly M unique 
characters. If there are more than one substring of longest possible length, then 
print any one of them.
Examples:

"aabbcc", k = 1
Max substring can be any one from {"aa" , "bb" , "cc"}.

"aabbcc", k = 2
Max substring can be any one from {"aabb" , "bbcc"}.

"aabbcc", k = 3
There are substrings with exactly 3 unique characters
{"aabbcc" , "abbcc" , "aabbc" , "abbc" }
Max is "aabbcc" with length 6.

"aaabbb", k = 3
There are only two unique characters, thus show error message. 
'''

def process(word, k):
    if len(word) == 0 or len(set(word)) < k: # not possible
        return -1
    
    char_map = defaultdict(lambda: 0)
    count, start, end = 1, 0, 0
    ans, string = 0, ""

    for i in range(1, len(word)):
        if word[i] != word[i-1]
            count += 1
        
        char_map[word[i]] += 1
        end += 1
        
        if count > k:
            ans = max(ans, end - start)
            while sum([1 for key in char_map.keys() if char_map[key] > 0]) > k:
                char_map[word[start]] -= 1
                start += 1

        if ans < (end - start + 1):
            ans = end - start + 1
            string = word[start: end + 1]
    return string




    