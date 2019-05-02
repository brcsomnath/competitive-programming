'''
159. Longest Substring with At Most Two Distinct Characters

Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
For example, Given s = “eceba”,

T is "ece" which its length is 3
'''

def main():
    word = input()
    character_dict = {}
    index_array = [-1]*len(word)

    start = 0
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            index_array[i] = start
            continue
        index_array[i] = i
        start = i

        

    start, max_len = 0, 0

    temp_dict = []
    for i in range(len(word)):
        if word[i] not in temp_dict:
            temp_dict.append(word[i])
        
            if len(temp_dict) > 2:
                max_len = max(max_len, i - start)
                print(i, start, max_len)
                temp_dict = [word[i-1], word[i]]
                start = index_array[i-1]

    max_len = max(max_len, (len(word) - start))
    print(max_len)
        
if __name__ == "__main__":
    main()