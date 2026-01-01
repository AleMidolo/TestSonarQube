def solve(self):
    """
        Utilizza l’algoritmo BFS per trovare un percorso che porti dallo stato iniziale allo stato obiettivo.Mantiene una lista come coda (open_list), inizialmente contenente lo stato iniziale. A ogni iterazione visita ed estrae l’elemento in posizione 0, richiama il metodo get_possible_moves per ottenere tutte le direzioni possibili e, per ciascuna di esse, invoca move per generare i nuovi stati, che vengono poi aggiunti alla coda. Il processo continua finché open_list non è vuota oppure finché non si raggiunge lo stato obiettivo.
        :return path: lista di str, la soluzione allo stato obiettivo.
        >>> eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        >>> eightPuzzle.solve()
        ['destra']
        """
    from collections import deque
    open_list = deque([(self.initial_state, [])])
    visited = set()
    visited.add(tuple(map(tuple, self.initial_state)))
    while open_list:
        current_state, path = open_list.popleft()
        if current_state == self.goal_state:
            return path
        for move_direction in self.get_possible_moves(current_state):
            new_state = self.move(current_state, move_direction)
            new_path = path + [move_direction]
            if tuple(map(tuple, new_state)) not in visited:
                visited.add(tuple(map(tuple, new_state)))
                open_list.append((new_state, new_path))
    return []