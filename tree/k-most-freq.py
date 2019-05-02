from collections import defaultdict
import heapq

def k_most_freq(input):
    count = defaultdict(lambda: 0)
    for x in input:
        count[x] += 1
    
    list_of_vals = []
    for k in count.keys():
        heapq.heappush(list_of_vals, k)
        if len(list_of_vals) > N:
            heapq._heappop_max(list_of_vals)
    
    return list_of_vals

    
