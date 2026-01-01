def book_ticket(self, name, seats_to_book):
    """
        Prenota i biglietti per un film. Cambia il valore dei posti in self.movies se la prenotazione ha successo.
        :param name: str, nome del film
        :param seats_to_book: lista di tuple, che rappresentano i posti da prenotare [(riga1, colonna1), (riga2, colonna2), ...]
        :return: str, messaggio di stato della prenotazione. "Film non trovato." se non esiste un film del genere.
                "Prenotazione riuscita." per una prenotazione avvenuta con successo, o "Prenotazione fallita." altrimenti
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.book_ticket('Batman', [(0, 0), (0, 1)])
        'Prenotazione riuscita.'
        >>> system.book_ticket('Batman', [(0, 0)])
        'Prenotazione fallita.'
        >>> system.book_ticket('batman', [(0, 0)])
        'Film non trovato.'
        """
    movie = None
    for m in self.movies:
        if m['name'] == name:
            movie = m
            break
    if movie is None:
        return 'Film non trovato.'
    seats_array = movie['seats']
    n_rows, n_cols = seats_array.shape
    for row, col in seats_to_book:
        if row < 0 or row >= n_rows or col < 0 or (col >= n_cols):
            return 'Prenotazione fallita.'
        if seats_array[row, col] != 0:
            return 'Prenotazione fallita.'
    for row, col in seats_to_book:
        seats_array[row, col] = 1
    return 'Prenotazione riuscita.'