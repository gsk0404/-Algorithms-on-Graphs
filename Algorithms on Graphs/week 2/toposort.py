# Uses python3
import sys
sys.setrecursionlimit(200000)

def dfs(adj, used, order, v):
    used[v] = True
    for u in adj[v]:
        if not used[u]:
            dfs(adj, used, order, u)
    order.append(v)

def toposort(adj):
    used = [False] * len(adj)
    order = []
    for v in range(len(adj)):
        if not used[v]:
            dfs(adj, used, order, v)
    return [x+1 for x in reversed(order)]

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
    result = toposort(adj)
    print(' '.join(map(str, result)))
