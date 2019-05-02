'''
Given a string, check if it is can be reorganized such that
the same char is not next to each other,
If possible, output a possible result example 

input: google 
one possible output: gogole
'''

def validate(word):
    char_map = [0]*26

    for w in word:
        char_map[ord(w) - ord('a')] += 1
    
    arr = []
    for i in range(len(char_map)):
        if char_map[i] > 0:
            arr.append(char_map[i])

    arr.sort(reverse=True)

    empty_space = 0
    for num in arr:
        element = num

        if element > empty_space:
            empty_space = element - empty_space - 1
        else:
            empty_space -= element
    
    if empty_space > 0:
        return False
    return True

def main():
    print(validate('gooooooogle'))

if __name__ == "__main__":
    main()