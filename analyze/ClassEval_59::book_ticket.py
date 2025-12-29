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
    for movie in self.movies:
        if movie['name'].lower() == name.lower():
            for seat in seats_to_book:
                row, col = seat
                if movie['seats'][row, col] == 0:
                    movie['seats'][row, col] = 1
                else:
                    return 'Prenotazione fallita.'
            return 'Prenotazione riuscita.'
    return 'Film non trovato.'