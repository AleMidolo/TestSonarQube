def solve(self):
    """
        Utiliza el algoritmo BFS para encontrar la solución del camino que lleva el estado inicial al estado objetivo.
        Mantiene una lista como una cola, llamada open_list, y agrega el estado inicial.
        Siempre visita y elimina el elemento en el índice 0, invoca el método get_possible_moves para encontrar todas las direcciones posibles.
        Recorre la lista possible_moves e invoca el método move para obtener varios nuevos estados. Luego los agrega.
        Repite los pasos anteriores hasta que open_list esté vacía o el estado haya cambiado al estado objetivo.
        :return path: lista de str, la solución al estado objetivo.
        >>> eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        >>> eightPuzzle.solve()
        ['derecha']
        """
    from collections import deque
    start_state = tuple((tuple(row) for row in self.initial_state))
    goal_state = tuple((tuple(row) for row in self.goal_state))
    queue = deque()
    queue.append((start_state, []))
    visited = set()
    visited.add(start_state)
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path
        current_state_list = [list(row) for row in current_state]
        possible_moves = self.get_possible_moves(current_state_list)
        for move in possible_moves:
            new_state_list = self.move(current_state_list, move)
            new_state = tuple((tuple(row) for row in new_state_list))
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [move]))
    return None