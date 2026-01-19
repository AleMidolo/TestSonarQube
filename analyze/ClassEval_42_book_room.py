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
    """
    # Controlla se il room_type esiste in available_rooms
    if room_type not in self.available_rooms:
        return False
    
    # Ottieni il numero di camere disponibili
    available = self.available_rooms[room_type]
    
    # Se non ci sono camere disponibili
    if available == 0:
        return False
    
    # Se il numero richiesto supera le camere disponibili
    if room_number > available:
        return available
    
    # Se ci sono abbastanza camere disponibili
    # Aggiorna available_rooms
    self.available_rooms[room_type] -= room_number
    
    # Aggiorna booked_rooms
    if room_type not in self.booked_rooms:
        self.booked_rooms[room_type] = []
    
    self.booked_rooms[room_type].append({
        'name': name,
        'rooms': room_number
    })
    
    return 'Successo!'