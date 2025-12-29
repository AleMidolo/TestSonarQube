def book_room(self, room_type, room_number, name):
    """
        Controlla se ci sono camere disponibili del tipo specificato.
        Se le camere sono adeguate, modifica available_rooms e booked_rooms e completa la prenotazione, altrimenti fallisce la prenotazione.
        :param room_type: str
        :param room_number: int, il numero previsto di camere del tipo specificato da prenotare
        :param name: str, nome dell'ospite
        :return: se il numero di camere che si sta per prenotare non supera le camere rimanenti, restituisce str 'Successo!'
                se supera ma la quantità di camere disponibili non è zero, restituisce int(la quantità rimanente di questo tipo di camera).
                se supera e la quantità è zero o il room_type non è in available_room, restituisce False.
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.book_room('single', 1, 'guest 1')
        'Successo!'
        >>> hotel.book_room('single', 5, 'guest 1')
        4
        >>> hotel.book_room('single', 4, 'guest 1')
        'Successo!'
        >>> hotel.book_room('single', 1, 'guest 1')
        False
        >>> hotel.book_room('triple', 1, 'guest 1')
        False
        """
    if room_type not in self.available_rooms:
        return False
    available = self.available_rooms[room_type]
    if available == 0:
        return False
    if room_number <= available:
        self.available_rooms[room_type] -= room_number
        if room_type not in self.booked_rooms:
            self.booked_rooms[room_type] = {}
        if name in self.booked_rooms[room_type]:
            self.booked_rooms[room_type][name] += room_number
        else:
            self.booked_rooms[room_type][name] = room_number
        return 'Successo!'
    else:
        return available