'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
 find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

'''

import sys
from queue import PriorityQueue

def process(meetings):
    meetings = sorted(meetings, key = lambda x: x[0])
    count = 1

    pq = PriorityQueue()
    pq.put(meetings[0][1])

    for i in range(1, len(meetings)):
        min_end = pq.get()
        if min_end <= meetings[i][0]:
            min_end = meetings[i][1]
        else:
            count += 1
            pq.put(meetings[i][1])
        pq.put(min_end)
    return count

def main():
    meetings = [[0, 30],[5, 10],[15, 20]]
    # for line in sys.stdin:
    #     meetings.append([int(element) for element in line.strip().split()])
    print(process(meetings))

if __name__ == "__main__":
    main()