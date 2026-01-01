def get_available_rooms(self, room_type):
    """
        Obtiene el número de habitaciones disponibles de un tipo específico.
        :param room_type: str, el tipo de habitación del que se desea conocer la disponibilidad
        :return: int, el número restante de habitaciones de este tipo.
        >>> hotel = Hotel('hotel paz', {'single': 5, 'double': 3})
        >>> hotel.get_available_rooms('single')
        5
        """
    if room_type in self.available_rooms:
        return self.available_rooms[room_type]
    else:
        return 0