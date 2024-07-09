"""Implementação do algoritmo 'branch and bound'."""

class Node:
    def __init__(self, level, path, bound, cost):
        self.level = level
        self.path = path
        self.bound = bound
        self.cost = cost

def tsp_bound(node, n, adj):
    bound = node.cost
    min_out = [float('inf')] * n
    for i in range(n):
        for j in range(n):
            if adj[i][j] < min_out[i]:
                min_out[i] = adj[i][j]
    bound += sum(min_out)
    return bound

def branch_and_bound(graph, start: int, goal: int) -> (int, float, [int]):
    n = len(graph)
    root = Node(0, [start], 0, 0)
    root.bound = tsp_bound(root, n, graph)
    queue = [root]
    best_cost = float('inf')
    best_path = None
    evaluated_vertices = []
    num_evaluated_vertices = 0

    while queue:
        node = queue.pop(0)
        evaluated_vertices.append(node.path[-1])
        num_evaluated_vertices += 1
        if node.bound < best_cost:
            for i in range(n):
                if i not in node.path:
                    new_path = node.path + [i]
                    new_cost = node.cost + graph[node.path[-1]][i]
                    if len(new_path) == n and i == goal:
                        new_cost += graph[new_path[-1]][start]
                        if new_cost < best_cost:
                            best_cost = new_cost
                            best_path = new_path
                    else:
                        new_node = Node(node.level + 1, new_path, 0, new_cost)
                        new_node.bound = tsp_bound(new_node, n, graph)
                        if new_node.bound < best_cost:
                            queue.append(new_node)
    return num_evaluated_vertices, best_cost, best_path
