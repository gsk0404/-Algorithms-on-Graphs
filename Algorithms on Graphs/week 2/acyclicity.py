# Uses python3
import sys
sys.setrecursionlimit(200000)

def dfs(adj, visited, rec_stack, v):
    visited[v] = True
    rec_stack[v] = True
    for u in adj[v]:
        if not visited[u]:
            if dfs(adj, visited, rec_stack, u):
                return True
        elif rec_stack[u]:
            return True
    rec_stack[v] = False
    return False

def acyclic(adj):
    n = len(adj)
    visited = [False] * n
    rec_stack = [False] * n
    for v in range(n):
        if not visited[v]:
            if dfs(adj, visited, rec_stack, v):
                return 1
    return 0

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
    print(acyclic(adj))
