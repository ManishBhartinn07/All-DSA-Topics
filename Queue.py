from collections import deque

def solve(q):
    n=len(q)
    for _ in range(n):
        e=q.pop()
        q.appendleft(e)
    return q
queue = deque([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# k = 5

print(solve(queue))