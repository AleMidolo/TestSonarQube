def solve(self):
    """
        Utilizza l’algoritmo BFS per trovare un percorso che porti dallo stato iniziale allo stato obiettivo.Mantiene una lista come coda (open_list), inizialmente contenente lo stato iniziale. A ogni iterazione visita ed estrae l’elemento in posizione 0, richiama il metodo get_possible_moves per ottenere tutte le direzioni possibili e, per ciascuna di esse, invoca move per generare i nuovi stati, che vengono poi aggiunti alla coda. Il processo continua finché open_list non è vuota oppure finché non si raggiunge lo stato obiettivo.
        :return path: lista di str, la soluzione allo stato obiettivo.
        >>> eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        >>> eightPuzzle.solve()
        ['destra']
        """
    from collections import deque
    start = tuple((tuple(row) for row in self.initial_state))
    goal = tuple((tuple(row) for row in self.goal_state))
    queue = deque()
    queue.append((start, []))
    visited = set()
    visited.add(start)
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal:
            italian_path = []
            for direction in path:
                if direction == 'right':
                    italian_path.append('destra')
                elif direction == 'left':
                    italian_path.append('sinistra')
                elif direction == 'up':
                    italian_path.append('su')
                elif direction == 'down':
                    italian_path.append('giù')
            return italian_path
        current_state_list = [list(row) for row in current_state]
        possible_moves = self.get_possible_moves(current_state_list)
        for move in possible_moves:
            new_state_list = self.move(current_state_list, move)
            new_state = tuple((tuple(row) for row in new_state_list))
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [move]))
    return []