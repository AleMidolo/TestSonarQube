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
    
    # Inicializar la cola con el estado inicial
    open_list = deque()
    open_list.append((self.state, []))  # (estado_actual, camino_hasta_aquí)
    
    # Conjunto para rastrear estados visitados
    visited = set()
    visited.add(str(self.state))
    
    while open_list:
        # Visitar y eliminar el elemento en el índice 0
        current_state, path = open_list.popleft()
        
        # Verificar si hemos alcanzado el estado objetivo
        if current_state == self.goal_state:
            return path
        
        # Guardar el estado actual temporalmente
        original_state = self.state
        self.state = current_state
        
        # Obtener todos los movimientos posibles
        possible_moves = self.get_possible_moves()
        
        # Recorrer cada movimiento posible
        for direction in possible_moves:
            # Realizar el movimiento para obtener el nuevo estado
            new_state = self.move(direction)
            
            # Verificar si el nuevo estado no ha sido visitado
            state_str = str(new_state)
            if state_str not in visited:
                visited.add(state_str)
                # Agregar el nuevo estado a la cola con el camino actualizado
                new_path = path + [direction]
                open_list.append((new_state, new_path))
        
        # Restaurar el estado original
        self.state = original_state
    
    # Si open_list está vacía y no se encontró solución
    return []