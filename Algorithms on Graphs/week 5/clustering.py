# Uses python3
import math

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root != v_root:
            if self.rank[u_root] < self.rank[v_root]:
                self.parent[u_root] = v_root
            else:
                self.parent[v_root] = u_root
                if self.rank[u_root] == self.rank[v_root]:
                    self.rank[u_root] += 1

def clustering(x, y, k):
    n = len(x)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            dist = math.hypot(x[i] - x[j], y[i] - y[j])
            edges.append((dist, i, j))
    edges.sort()
    dsu = DisjointSet(n)
    num_clusters = n
    for edge in edges:
        if dsu.find(edge[1]) != dsu.find(edge[2]):
            if num_clusters == k:
                return edge[0]
            dsu.union(edge[1], edge[2])
            num_clusters -= 1
    return -1

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = list(map(float, input().split()))
    n = int(data[0])
    x = []
    y = []
    for i in range(n):
        x.append(data[1 + 2 * i])
        y.append(data[2 + 2 * i])
    k = int(data[-1])
    print("{0:.9f}".format(clustering(x, y, k)))
