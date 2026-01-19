def book_ticket(self, name, seats_to_book):
    """
    Reserva boletos para una película. Cambia el valor de los asientos en self.movies si se reserva con éxito.
    :param name: str, nombre de la película
    :param seats_to_book: lista de tuplas, representando los asientos a reservar [(fila1, col1), (fila2, col2), ...]
    :return: str, mensaje de estado de la reserva. "Película no encontrada." si no existe tal película.
            "Reserva exitosa." si se reserva con éxito, o "Reserva fallida." en caso contrario
    >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
    >>> system.book_ticket('Batman', [(0, 0), (0, 1)])
    'Reserva exitosa.'
    >>> system.book_ticket('Batman', [(0, 0)])
    'Reserva fallida.'
    >>> system.book_ticket('batman', [(0, 0)])
    'Película no encontrada.'
    """
    # Check if movie exists
    if name not in self.movies:
        return "Película no encontrada."
    
    movie = self.movies[name]
    seats = movie['seats']
    
    # Check if all seats are available (value is 0)
    for row, col in seats_to_book:
        # Check if indices are valid
        if row < 0 or row >= len(seats) or col < 0 or col >= len(seats[0]):
            return "Reserva fallida."
        # Check if seat is already booked (not 0)
        if seats[row][col] != 0:
            return "Reserva fallida."
    
    # All seats are available, proceed with booking
    for row, col in seats_to_book:
        seats[row][col] = 1  # Mark seat as booked
    
    return "Reserva exitosa."