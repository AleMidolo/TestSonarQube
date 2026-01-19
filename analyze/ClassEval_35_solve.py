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
    # Initialize open_list with initial state and empty path
    open_list = [(self, [])]
    visited = set()
    
    while open_list:
        # Pop the first element (index 0) from open_list
        current_state, path = open_list.pop(0)
        
        # Check if current state is goal state
        if current_state.is_goal():
            return path
        
        # Convert current state to tuple for visited tracking
        state_tuple = tuple(tuple(row) for row in current_state.state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        
        # Get all possible moves
        possible_moves = current_state.get_possible_moves()
        
        # Traverse through possible_moves
        for direction in possible_moves:
            # Create new state by moving in the direction
            new_state = current_state.move(direction)
            
            # Add new state to open_list with updated path
            if new_state is not None:
                new_path = path + [direction]
                open_list.append((new_state, new_path))
    
    # Return empty list if no solution found
    return []