# Uses python3
import sys
sys.setrecursionlimit(100000)

def explore(adj, visited, v):
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            explore(adj, visited, u)

def number_of_components(adj):
    visited = [False] * len(adj)
    result = 0
    for v in range(len(adj)):
        if not visited[v]:
            explore(adj, visited, v)
            result += 1
    return result

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
    print(number_of_components(adj))
