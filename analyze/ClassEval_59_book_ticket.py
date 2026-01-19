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
    # Verifica se il film esiste
    if name not in self.movies:
        return "Film non trovato."
    
    movie = self.movies[name]
    seats = movie['seats']
    
    # Verifica che tutti i posti richiesti siano disponibili
    for row, col in seats_to_book:
        # Controlla se gli indici sono validi
        if row < 0 or row >= len(seats) or col < 0 or col >= len(seats[0]):
            return "Prenotazione fallita."
        # Controlla se il posto è già occupato (True significa occupato)
        if seats[row][col]:
            return "Prenotazione fallita."
    
    # Se tutti i posti sono disponibili, procedi con la prenotazione
    for row, col in seats_to_book:
        seats[row][col] = True
    
    return "Prenotazione riuscita."