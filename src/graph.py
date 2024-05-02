"""Implementação de uma estrutura de grafo."""


def read_graph(file_path):
    """Implementação de uma estrutura de grafo."""
    # pylint: disable=unused-variable
    with open(file_path, encoding="utf-8") as file:
        lines = file.read().strip().split("\n")
    num_nodes = int(lines[0])
    nodes = {i: tuple(map(float, line.split()[1:]))  # noqa
             for i, line in enumerate(
                 lines[1:num_nodes+1]
                 )}
    num_edges = int(lines[num_nodes+1]) # noqa
    edges = [tuple(map(float, line.split()))
             for line in lines[num_nodes+2:]]
    graph = {i: [] for i in range(num_nodes)}
    for node1, node2, cost in edges:
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))
    return graph
