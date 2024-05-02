"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import a_star


if __name__ == "__main__":
    GRAFO = read_graph("./mapas/small_map.txt")
    print("Exemplo 1: ")
    print(a_star(GRAFO, 0, 764))
    print("Exemplo 2: ")
    print(a_star(GRAFO, 230, 850))
    print("Exemplo 3: ")
    print(a_star(GRAFO, 0, 20))
    print("Exemplo 4: ")
    print(a_star(GRAFO, 0, 6))
    print("Exemplo 5: ")
    print(a_star(GRAFO, 6, 0))
