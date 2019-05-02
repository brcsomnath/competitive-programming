'''
359. Logger Rate Limiter

Design a logger system that receive stream of messages along with its timestamps,
 each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message
should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.
'''
from collections import defaultdict
from queue import *

msg_dict = defaultdict(lambda: 0)
q = deque()
pq = PriorityQueue()

def peek(pq):
    return pq.queue[0][0]

def logger(message, timestamp):
    while not pq.empty() and peek(pq) < timestamp - 10:
        _, msg = pq.get()
        msg_dict[msg] -= 1
    
    if msg_dict[msg] == 0:
        msg_dict[msg] += 1
        pq.put((timestamp, msg))
        return True
    return False
