# Uses python3
import math

def minimum_distance(x, y):
    n = len(x)
    points = [(x[i], y[i]) for i in range(n)]
    cost = [float('inf')] * n
    in_tree = [False] * n
    cost[0] = 0
    result = 0
    for _ in range(n):
        u = -1
        for i in range(n):
            if not in_tree[i] and (u == -1 or cost[i] < cost[u]):
                u = i
        result += cost[u]
        in_tree[u] = True
        for v in range(n):
            if not in_tree[v]:
                d = math.hypot(points[u][0] - points[v][0], points[u][1] - points[v][1])
                if cost[v] > d:
                    cost[v] = d
    return result

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    n = data[0]
    x = []
    y = []
    for i in range(n):
        x.append(data[1 + 2 * i])
        y.append(data[2 + 2 * i])
    print("{0:.9f}".format(minimum_distance(x, y)))
