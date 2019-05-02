'''
Sentence Similarity II

Given two sentences words1, words2 (each represented as an array of strings),
 and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"]
 are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"],
  ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar,
 and "fine" and "good" are similar, then "great" and "fine" are similar
'''

from collections import defaultdict

parent = defaultdict(lambda: -1)

def find_parent(node):
    if parent[node] == -1 or parent[node] == node:
        return node
    return find_parent(parent[node])

def union(src, dest):
    src_parent = find_parent(src)
    dest_parent = find_parent(dest)
    if src_parent != dest_parent:
        parent[src_parent] = dest_parent

def union_find(pairs):
    for pair in pairs:
        src, dest = pair
        union(src, dest)

def process(words1, words2, pairs):
    if len(words1) != len(words2):
        return False

    union_find(pairs)
    print(parent)
    for i in range(len(words1)):
        if find_parent(words1[i]) != find_parent(words2[i]):
            return False
    return True

def main():
    words1 = input().split()
    words2 = input().split()
    pairs = []

    inp = input().split()
    while len(inp) > 0:
        pairs.append(inp)
        inp = input().split()
    
    print(process(words1, words2, pairs))
    
if __name__ == "__main__":
    main()