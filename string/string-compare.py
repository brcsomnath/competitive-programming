from collections import defaultdict
import itertools

def get_signature(word):
    x = [0]*26
    for w in list(word):
        x[ord(w) - 97] += 1
    return x

def get_index(m, n):
    for i in range(len(m)):
        if abs(m[i] - n[i]) > 0:
            return chr(97+i)

def get_index_(a, b):
    mp_a = defaultdict(lambda:0)
    mp_b = defaultdict(lambda:0)

    for i in a:
        mp_a[i]+=1
    
    for i in b:
        mp_b[i]+=1

    keys = set(itertools.chain(mp_a.keys(), mp_b.keys()))

    for k in keys:
        if (k in mp_a.keys() and k not in mp_b.keys()) or (k not in mp_a.keys() and k in mp_b.keys()):
            return k


def main():
    a, b = input().split()
    print(get_index_(a, b))


if __name__ == '__main__':
    main()