def check_in(self, room_type, room_number, name):
    """
    Controlla se la stanza del tipo e numero specificati è prenotata dalla persona di nome name.
    Rimuovi questo nome quando il check-in è avvenuto con successo (room_number è uguale alle booked_rooms di una persona specifica). Quando la quantità effettiva del check-in (room_number) è inferiore alla quantità prenotata, il numero in booked_rooms sarà la quantità prenotata meno la quantità effettiva.
    :param room_type: str, tipo di stanza per il check-in
    :param room_number: int, numero della stanza per il check-in
    :param name: str, nome della persona
    :return False: solo se il room_type non è nelle booked_rooms o se room_number è superiore alla quantità nelle booked_rooms.
    >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
    >>> hotel.book_room('single', 1, 'guest 1')
    'Successo!'
    >>> hotel.check_in('single', 2, 'guest 1')
    False
    >>> hotel.check_in('single', 1, 'guest 1')
    >>> hotel.booked_rooms
    {'single': {}}
    """
    # Verifica se il room_type esiste nelle booked_rooms
    if room_type not in self.booked_rooms:
        return False
    
    # Verifica se il nome esiste nelle prenotazioni per questo tipo di stanza
    if name not in self.booked_rooms[room_type]:
        return False
    
    # Ottieni il numero di stanze prenotate da questa persona
    booked_count = self.booked_rooms[room_type][name]
    
    # Verifica se room_number è superiore alla quantità prenotata
    if room_number > booked_count:
        return False
    
    # Se room_number è uguale alla quantità prenotata, rimuovi completamente la prenotazione
    if room_number == booked_count:
        del self.booked_rooms[room_type][name]
    else:
        # Altrimenti, riduci la quantità prenotata
        self.booked_rooms[room_type][name] = booked_count - room_number