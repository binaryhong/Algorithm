from collections import deque

def solution(x, y, n):
    queue = deque([(x, 0)])
    visited = set()
    while queue:
        curr, count = queue.popleft()
        if curr == y:
            return count
        if curr in visited:
            continue
        visited.add(curr)
        if curr + n <= y:
            queue.append((curr + n, count + 1))
        if curr * 2 <= y:
            queue.append((curr * 2, count + 1))
        if curr * 3 <= y:
            queue.append((curr * 3, count + 1))
    return -1
