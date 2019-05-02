from math import log2

POWER = [2 ** i for i in range(1, steps + 1)]

class Suffix():
    def __init__(self, idx, first, second):
        self.index = idx
        self.first = first
        self.second = second

# Building the suffix array takes O(N(log N)^2)
def build_tree(word):
    N = len(word)
    steps = int(log2(N))

    P = [[-1 for i in range(N+1)] for j in range(steps)]

    for i in range(N):
        P[0][i] = ord(word[i]) - ord('a')

    L = [()] * (N+1)

    for step in range(1, steps):
        for j in range(N):
            index = j # previous rank
            # rank from last step (2^k chars)
            first = P[step-1][j] 
            # rank for next step (upcoming 2^k chars)
            second = P[step-1][j+POWER[step-1]] if j+POWER[step-1]<=n else -1) 
            L[j] = (index, first, second)

        L.sort()
        for j in range(1, N+1):
            # update the table using the sorted array
            P[step][L[j].index] = P[step][L[j-1].index] if j>1 and L[j].first==L[j-1].first and L[j].second==L[j-1].second else j      

    SA = [0] * N
    for i in range(1, N+1)
        SA[P[steps - 1][i]] = i

# O(log N) complexity
def LCP(i,j): # returns the length of LCP of suffixes starting at indices i and j

    if i == j:
        return N-i+1

    return_value =0

    for x in range(step, -1, -1):
        if P[x][i]==P[x][j] and i < N and j < N:
            return_value = return_value + POWER[x]
            i = i + POWER[x]
            j = j + POWER[x]

    return return_value