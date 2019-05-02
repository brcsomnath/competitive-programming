from collections import defaultdict
from queue import Queue

class Solution:
    def check_diff(self, word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
            
            if diff > 1:
                return False
        return diff == 1
    
    def bfs(self, graph, src, dest):
        q = Queue()
        q.put(src)
        
        dist = defaultdict(lambda: float('inf'))
        visited = defaultdict(lambda: False)
        dist[src] = 0
        
        while not q.empty():
            u = q.pop()
            
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    dist[v] = min(dist[v], dist[u] + 1)
                    q.put(v)
        return dist[dest]
            
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        
        wordList.append(beginWord)
        wordList = list(set(wordList))
        
        N = len(wordList)
        for i in range(N-1):
            for j in range(i+1, N):
                if self.check_diff(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        
        visited = defaultdict(lambda: False)
        dist = defaultdict(lambda: float('inf'))
        d = self.bfs(graph, beginWord, endWord):
        return d if d < float('inf') else 0
                    
        
                