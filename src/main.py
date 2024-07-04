"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import dfs


if __name__ == "__main__":
    GRAFO = read_graph("./mapas/small_map.txt")
    print("Exemplo 1: ")
    print(dfs(GRAFO, 0, 764))
    print("Exemplo 2: ")
    print(dfs(GRAFO, 230, 850))
    print("Exemplo 3: ")
    print(dfs(GRAFO, 0, 20))
    print("Exemplo 4: ")
    print(dfs(GRAFO, 0, 6))
    print("Exemplo 5: ")
    print(dfs(GRAFO, 6, 0))
