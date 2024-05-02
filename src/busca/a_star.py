"""Implementação do algoritmo A*."""
import heapq


def a_star(graph, start: int, goal: int) -> (int, float, [int]):  
    """Implementação do algoritmo A*."""
    # type: ignore comment;

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
            return len(path), cost_so_far[goal], path
    # Comparado com o código antigo, essa parte teve algumas mudanças de
    # otimização e simplificou bastante. Essa linha inicia um loop sobre
    # cada vizinho do nó atual.
        for neighbor, cost in graph[current]:
            # Essa linha calcula o custo total para chegar ao nó vizinho
            # partir do nó inicial.
            new_cost = cost_so_far[current] + cost
            # Essa linha verifica se o nó vizinho já foi visitado.
            # Se não foi, ou se o novo custo calculado é menor do que o custo
            # registrado anteriormente para chegar ao nó vizinho, então
            # o código vai atualizar o custo e a rota.
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                # Essa linha atualiza o custo para chegar ao nó vizinho com o
                # novo custo calculado.
                cost_so_far[neighbor] = new_cost
                # Essa linha define a prioridade do nó vizinho como o
                # novo custo.
                priority = new_cost
                # Essa linha adiciona o nó vizinho à lista de nós a
                # serem visitados
                heapq.heappush(open_list, (priority, neighbor))
                # Essa linha registra que o nó atual é o nó a partir do qual
                # chegamos ao nó vizinho.
                came_from[neighbor] = current

    return "Não foi possível encontrar um caminho."
