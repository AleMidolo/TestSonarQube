def check_out(self, room_type, room_number):
        """
        Effettua il check-out delle stanze, aggiungendo il numero per il tipo specifico in available_rooms.
        Se room_type è nuovo, aggiungi un nuovo tipo in available_rooms.
        :param room_type: str, tipo di stanza da effettuare il check-out
        :param room_number: int, numero della stanza da effettuare il check-out
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.check_out('single', 2)
        >>> hotel.available_rooms
        {'single': 7, 'double': 3}
        >>> hotel.check_out('triple', 2)
        >>> hotel.available_rooms
        {'single': 7, 'double': 3, 'triple': 2}
        """
        if room_type in self.available_rooms:
            self.available_rooms[room_type] += room_number
        else:
            self.available_rooms[room_type] = room_number