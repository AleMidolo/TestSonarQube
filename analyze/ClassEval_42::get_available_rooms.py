def get_available_rooms(self, room_type):
    """
        Ottieni il numero di stanze disponibili di un tipo specifico.
        :param room_type: str, il tipo di stanza di cui si desidera conoscere la disponibilità
        :return: int, il numero rimanente di stanze di questo tipo.
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.get_available_rooms('single')
        5
        """
    if room_type in self.available_rooms:
        return self.available_rooms[room_type]
    else:
        return 0