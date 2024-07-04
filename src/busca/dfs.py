"""Implementação da busca em profundidade."""

# from util import reverse_path


def dfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em profundidade."""
    if start not in goal:
        print(start, end=' ')
        goal.add(start)
        for vizinho in graph[start] - goal:
            dfs(graph, vizinho, goal)
