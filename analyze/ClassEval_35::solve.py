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
    if self.initial_state == self.goal_state:
        return []
    queue = deque()
    visited = set()
    initial_state_tuple = tuple((tuple(row) for row in self.initial_state))
    queue.append((self.initial_state, []))
    visited.add(initial_state_tuple)
    while queue:
        current_state, path = queue.popleft()
        if current_state == self.goal_state:
            return path
        possible_moves = self.get_possible_moves(current_state)
        for move in possible_moves:
            new_state = self.move(current_state, move)
            new_state_tuple = tuple((tuple(row) for row in new_state))
            if new_state_tuple not in visited:
                visited.add(new_state_tuple)
                queue.append((new_state, path + [move]))
    return None