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
    
    # Initialize open_list as a queue with the initial state
    # Each element is a tuple: (current_state, path_to_reach_this_state)
    open_list = [(self, [])]
    
    # Keep track of visited states to avoid cycles
    visited = set()
    visited.add(str(self.state))
    
    while open_list:
        # Pop the first element (BFS - FIFO)
        current_puzzle, path = open_list.pop(0)
        
        # Check if current state is the goal state
        if current_puzzle.is_goal():
            return path
        
        # Get all possible moves from current state
        possible_moves = current_puzzle.get_possible_moves()
        
        # Traverse through all possible moves
        for direction in possible_moves:
            # Create a new state by making the move
            new_puzzle = current_puzzle.move(direction)
            
            # Check if this state has been visited before
            state_str = str(new_puzzle.state)
            if state_str not in visited:
                visited.add(state_str)
                # Add the new state to open_list with updated path
                open_list.append((new_puzzle, path + [direction]))
    
    # If open_list is empty and no solution found
    return []