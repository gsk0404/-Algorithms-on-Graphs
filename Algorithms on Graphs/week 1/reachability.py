# Uses python3
import sys
sys.setrecursionlimit(100000)

def explore(adj, visited, v):
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            explore(adj, visited, u)

def reach(adj, x, y):
    visited = [False] * len(adj)
    explore(adj, visited, x)
    return 1 if visited[y] else 0

if __name__ == '__main__':
    input = sys.stdin.read
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    edges = []
    for i in range(m):
        edges.append((data[2 + 2*i], data[2 + 2*i + 1]))
    x, y = data[-2]-1, data[-1]-1
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    print(reach(adj, x, y))
