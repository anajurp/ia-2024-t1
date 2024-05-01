"""Implementação do algoritmo A*."""
import heapq


def a_star(graph, start: int, goal: int) -> (int, float, [int]):
    """
  Executa o algoritmo A* para encontrar o caminho mais curto entre um nó
  de partida e um nó de destino em um grafo.

  Parâmetros:
  - graph: O grafo representado como um dicionário, onde as chaves são os nós
  e os valores são listas de tuplas (vizinho, custo).
  - start: O nó de partida.
  - goal: O nó de destino.

  Retorna uma tupla contendo:
  - O custo total do caminho encontrado.
  - O tamanho do caminho encontrado.
  - A lista de nós que compõem o caminho encontrado.
  """
    open_list = [(0, start)]
    heapq.heapify(open_list)
    cost_so_far = {start: 0}
    came_from = {}

    # Laço igual ao código antigo.
    while open_list:
        _, current = heapq.heappop(open_list)

    if current == goal:
        path = []
        while current in came_from:
            path.insert(0, current)
            current = came_from[current]
        path.insert(0, start)
        return cost_so_far[goal], len(path), path

    # Comparado com o código antigo, essa parte teve algumas mudanças de
    # otimização e simplificou bastante.
    # Essa linha inicia um loop sobre cada vizinho do nó atual.
    for neighbor, cost in graph[current]:
        # Essa linha calcula o custo total para chegar ao nó vizinho a partir
        # do nó inicial.
        new_cost = cost_so_far[current] + cost
        # Essa linha verifica se o nó vizinho já foi visitado.
        # Se não foi, ou se o novo custo calculado é menor do que o custo
        # registrado anteriormente para chegar ao nó vizinho, então o código
        # vai atualizar o custo e a rota.
        if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
            # Esta linha atualiza o custo para chegar ao nó vizinho com o novo
            # custo calculado.
            cost_so_far[neighbor] = new_cost
            # Esta linha define a prioridade do nó vizinho como o novo custo.
            priority = new_cost
            # Esta linha adiciona o nó vizinho à lista de nós a serem visitados
            heapq.heappush(open_list, (priority, neighbor))
            # Registra que o nó atual é o nó a partir do qual chegamos
            # ao nó vizinho.
            came_from[neighbor] = current

    return "Não foi possível encontrar um caminho."
