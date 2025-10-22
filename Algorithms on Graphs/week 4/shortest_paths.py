# Uses python3
import sys
from collections import deque

def shortest_paths(adj, cost, s, distance, reachable, shortest):
    n = len(adj)
    distance[s] = 0
    reachable[s] = 1

    # Bellman-Ford relaxations
    for _ in range(n - 1):
        for u in range(n):
            if distance[u] < float('inf'):
                for idx, v in enumerate(adj[u]):
                    if distance[v] > distance[u] + cost[u][idx]:
                        distance[v] = distance[u] + cost[u][idx]
                        reachable[v] = 1

    # Detect negative cycles
    affected = [False] * n
    for u in range(n):
        if distance[u] < float('inf'):
            for idx, v in enumerate(adj[u]):
                if distance[v] > distance[u] + cost[u][idx]:
                    affected[v] = True

    # Propagate negative cycle effect with BFS
    queue = deque([i for i, x in enumerate(affected) if x])
    while queue:
        u = queue.popleft()
        shortest[u] = 0
        for v in adj[u]:
            if shortest[v] == 1:
                shortest[v] = 0
                queue.append(v)

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
    s = data[idx]-1
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for (u, v, w) in edges:
        adj[u].append(v)
        cost[u].append(w)
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    for i in range(n):
        if not reachable[i]:
            print('*')
        elif not shortest[i]:
            print('-')
        else:
            print(distance[i])
