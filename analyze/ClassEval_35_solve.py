def solve(self):
    """
    Use BFS algorithm to find the path solution which makes the initial state to the goal method.
    Maintain a list as a queue, named as open_list, append the initial state.
    Always visit and pop the 0 index element, invoke get_possible_moves method find all the possible directions.
    Traversal the possible_moves list and invoke move method to get several new states.Then append them.
    redo the above steps until the open_list is empty or the state has changed to the goal state.
    :return path: list of str, the solution to the goal state.
    >>> eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
    >>> eightPuzzle.solve()
    ['right']
    """
    from collections import deque
    
    # Initialize the queue with the initial state and empty path
    open_list = deque([(self.state, [])])
    
    # Keep track of visited states to avoid cycles
    visited = set()
    visited.add(tuple(map(tuple, self.state)))
    
    while open_list:
        # Pop the first element (BFS uses FIFO)
        current_state, path = open_list.popleft()
        
        # Temporarily set the state to check if it's the goal
        original_state = self.state
        self.state = current_state
        
        # Check if current state is the goal state
        if self.is_goal():
            self.state = original_state
            return path
        
        # Get all possible moves from current state
        possible_moves = self.get_possible_moves()
        
        # Try each possible move
        for move in possible_moves:
            # Make the move to get new state
            new_state = self.move(move)
            
            # Check if this state has been visited
            state_tuple = tuple(map(tuple, new_state))
            if state_tuple not in visited:
                visited.add(state_tuple)
                # Append new state with updated path
                open_list.append((new_state, path + [move]))
            
            # Restore state for next iteration
            self.state = current_state
        
        # Restore original state
        self.state = original_state
    
    # No solution found
    return []