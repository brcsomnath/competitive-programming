
NEIGHBORS_MAP = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: tuple(),  # 5 has no neighbors
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6),
}

def neighbours(position):
    return NEIGHBORS_MAP[position]

def count_seq():
    dp = [0] * N
    dp[start] = 1

    for i in range(1, N):
        temp = dp
        for node in range(N):
            for neighbour in neighbours[node]:
                dp[node] += temp[neighbour]
        
    return sum(dp)