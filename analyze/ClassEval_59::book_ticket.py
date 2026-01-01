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
    movie = None
    for m in self.movies:
        if m['name'] == name:
            movie = m
            break
    if movie is None:
        return 'Película no encontrada.'
    seats_array = movie['seats']
    n_rows, n_cols = seats_array.shape
    for row, col in seats_to_book:
        if row < 0 or row >= n_rows or col < 0 or (col >= n_cols):
            return 'Reserva fallida.'
        if seats_array[row, col] != 0:
            return 'Reserva fallida.'
    for row, col in seats_to_book:
        seats_array[row, col] = 1
    return 'Reserva exitosa.'