def check_out(self, room_type, room_number):
    """
        Realiza el check-out de las habitaciones, añade el número para un tipo específico en available_rooms.
        Si room_type es nuevo, añade un nuevo tipo en available_rooms.
        :param room_type: str, tipo de habitación para el check-out
        :param room_number: int, número de habitación para el check-out
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