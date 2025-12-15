class EightPuzzle: 
    def __init__(self, initial_state):
        """
        Initializing the initial state of Eight Puzzle Game, stores in attribute self.initial_state.
        And set the goal state of this game, stores in self.goal_state. In this case, set the size as 3*3
        :param initial_state: a 3*3 size list of Integer, stores the initial state
        """
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def find_blank(self, state):
        """
        Find the blank position of current state, which is the 0 element.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return i, j: two Integers, represent the coordinate of the blank block.
        >>> eightPuzzle = EightPuzzle([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        >>> eightPuzzle.find_blank([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        (2, 1)
        """
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
        [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
        """
        i, j = self.find_blank(state)
        new_state = [row[:] for row in state]

        if direction == 'up':
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
        elif direction == 'down':
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
        elif direction == 'left':
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
        elif direction == 'right':
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]

        return new_state

    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        ['up', 'left', 'right']
        """
        moves = []
        i, j = self.find_blank(state)

        if i > 0:
            moves.append('up')
        if i < 2:
            moves.append('down')
        if j > 0:
            moves.append('left')
        if j < 2:
            moves.append('right')

        return moves

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