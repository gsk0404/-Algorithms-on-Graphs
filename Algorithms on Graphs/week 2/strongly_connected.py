# Uses python3
import sys
sys.setrecursionlimit(200000)

def dfs1(adj, used, order, v):
    used[v] = True
    for u in adj[v]:
        if not used[u]:
            dfs1(adj, used, order, u)
    order.append(v)

def dfs2(adj_r, component, v):
    component[v] = True
    for u in adj_r[v]:
        if not component[u]:
            dfs2(adj_r, component, u)

def number_of_strongly_connected_components(adj, adj_r):
    n = len(adj)
    used = [False]*n
    order = []
    for v in range(n):
        if not used[v]:
            dfs1(adj, used, order, v)
    component = [False]*n
    result = 0
    for v in reversed(order):
        if not component[v]:
            dfs2(adj_r, component, v)
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
    adj_r = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a-1].append(b-1)
        adj_r[b-1].append(a-1)
    print(number_of_strongly_connected_components(adj, adj_r))
