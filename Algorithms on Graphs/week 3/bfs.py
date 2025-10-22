# Uses python3
import sys
from collections import deque

def distance(adj, s, t):
    dist = [-1] * len(adj)
    dist[s] = 0
    queue = deque([s])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                queue.append(v)
                dist[v] = dist[u] + 1
    return dist[t]

if __name__ == '__main__':
    input = sys.stdin.read
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    edges = []
    for i in range(m):
        edges.append((data[2 + 2*i], data[2 + 2*i + 1]))
    s, t = data[-2] - 1, data[-1] - 1
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    print(distance(adj, s, t))
