# Uses python3
import sys

def negative_cycle(adj, cost):
    n = len(adj)
    dist = [0] * n
    for i in range(n):
        for u in range(n):
            for idx, v in enumerate(adj[u]):
                if dist[v] > dist[u] + cost[u][idx]:
                    dist[v] = dist[u] + cost[u][idx]
                    if i == n - 1:
                        return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    edges = []
    idx = 2
    for _ in range(m):
        u, v, w = data[idx]-1, data[idx+1]-1, data[idx+2]
        edges.append((u, v, w))
        idx += 3
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for (u, v, w) in edges:
        adj[u].append(v)
        cost[u].append(w)
    print(negative_cycle(adj, cost))
