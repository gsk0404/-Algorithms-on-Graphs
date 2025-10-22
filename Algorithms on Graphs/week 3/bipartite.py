# Uses python3
import sys
from collections import deque
sys.setrecursionlimit(200000)

def bipartite(adj):
    color = [None] * len(adj)
    for v in range(len(adj)):
        if color[v] is None:
            queue = deque([v])
            color[v] = 0
            while queue:
                u = queue.popleft()
                for w in adj[u]:
                    if color[w] is None:
                        color[w] = 1 - color[u]
                        queue.append(w)
                    elif color[w] == color[u]:
                        return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    edges = []
    for i in range(m):
        edges.append((data[2 + 2*i], data[2 + 2*i + 1]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    print(bipartite(adj))
