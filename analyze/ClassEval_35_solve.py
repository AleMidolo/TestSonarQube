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