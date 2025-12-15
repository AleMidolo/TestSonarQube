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
        BFS एल्गोरिदम का इस्तेमाल करके एक पाथ सॉल्यूशन ढूंढें जो गोल स्टेट तक पहुँचने के लिए
        शुरुआती स्टेट से चलने का रास्ता बताता है।

        open_list नाम की एक लिस्ट को क्यू के तौर पर बनाए रखें और शुरुआती स्टेट जोड़ें।
        हमेशा 0वें इंडेक्स एलिमेंट को पॉप करें और सभी संभावित डायरेक्शन ढूंढने के लिए
        get_possible_moves मेथड को इनवोक करें।

        possible_moves लिस्ट को ट्रैवर्स करें और कई नए स्टेट पाने के लिए move मेथड को इनवोक करें।
        फिर इन स्टेट्स को open_list में जोड़ें।

        ऊपर दिए गए स्टेप्स को तब तक दोहराएं जब तक open_list खाली न हो जाए या स्टेट गोल स्टेट में बदल न जाए।

        :return path: str की एक लिस्ट, जो गोल स्टेट तक पहुँचने का समाधान (path) दिखाती है।

        >>> eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        >>> eightPuzzle.solve()
        ['right']
        """
        from collections import deque

        open_list = deque([(self.initial_state, [])])
        visited = set()
        visited.add(tuple(map(tuple, self.initial_state)))

        while open_list:
            current_state, path = open_list.popleft()

            if current_state == self.goal_state:
                return path

            possible_moves = self.get_possible_moves(current_state)

            for move_direction in possible_moves:
                new_state = self.move(current_state, move_direction)
                new_state_tuple = tuple(map(tuple, new_state))

                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    open_list.append((new_state, path + [move_direction]))

        return []