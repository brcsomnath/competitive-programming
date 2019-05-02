'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".
'''

from collections import defaultdict

def topological_sort(graph, src, ans, visited):
    visited[src] = True

    for neighbour in graph[src]:
        if not visited[neighbour] 
            topological_sort(graph, neighbour, ans, visited)
    ans.append(src)

def process(dictionary):

    graph = defaultdict(list)

    for i in range(len(dictionary)):
        first_word = dictionary[i]

        pivot = first_word[0]
        for m in range(1, len(first_word)):
            if pivot != first_word[m] and first_word[m] not in graph[pivot]:
                graph[pivot].append(first_word[m])
            pivot = first_word[m]
                
        for j in range(i+1, len(dictionary)):
            second_word = dictionary[j]

            for k in range(len(first_word)):
                if k >= len(second_word):
                    break
                
                if first_word[i] != second_word[j] and first_word[i] not in graph[first_word[i]]:
                    graph[first_word[i]].append(second_word[i])

    vertices = len(graph.keys())
    ans = []
    visited = defaultdict(lambda: False)

    for vertex in graph.keys():
        if not visited[vertex]:
            topological_sort(graph, vertex, ans, visited)

    return ''.join(reversed(ans))

def main():
    dictionary = input().split()

if __name__ == "__main__":
    main()


    