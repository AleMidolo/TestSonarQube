def solve(self):
    """
        Utilizza l’algoritmo BFS per trovare un percorso che porti dallo stato iniziale allo stato obiettivo.Mantiene una lista come coda (open_list), inizialmente contenente lo stato iniziale. A ogni iterazione visita ed estrae l’elemento in posizione 0, richiama il metodo get_possible_moves per ottenere tutte le direzioni possibili e, per ciascuna di esse, invoca move per generare i nuovi stati, che vengono poi aggiunti alla coda. Il processo continua finché open_list non è vuota oppure finché non si raggiunge lo stato obiettivo.
        :return path: lista di str, la soluzione allo stato obiettivo.
        >>> eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        >>> eightPuzzle.solve()
        ['destra']
        """
    from collections import deque
    if self.initial_state == self.goal_state:
        return []
    queue = deque()
    queue.append((self.initial_state, []))
    visited = set()
    visited.add(tuple((tuple(row) for row in self.initial_state)))
    while queue:
        current_state, path = queue.popleft()
        if current_state == self.goal_state:
            return path
        possible_moves = self.get_possible_moves(current_state)
        for move in possible_moves:
            new_state = self.move(current_state, move)
            state_tuple = tuple((tuple(row) for row in new_state))
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append((new_state, path + [move]))
    return None