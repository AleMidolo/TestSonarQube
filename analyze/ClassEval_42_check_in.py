def check_in(self, room_type, room_number, name):
    """
    Verifica si la habitación del tipo y número especificados está reservada por la persona llamada name.
    Elimina este nombre cuando el check-in sea exitoso (room_number es igual a las booked_rooms de la persona específica). Cuando la cantidad real de check-in (room_number) es menor que la cantidad reservada, el número en booked_rooms será la cantidad reservada menos la cantidad real.
    :param room_type: str, tipo de habitación para el check-in
    :param room_number: int, número de habitación para el check-in
    :param name: str, nombre de la persona
    :return False: solo si el room_type no está en las booked_rooms o si room_number es mayor que la cantidad en las habitaciones reservadas.
    >>> hotel = Hotel('hotel paz', {'single': 5, 'double': 3})
    >>> hotel.book_room('single', 1, 'invitado 1')
    '¡Éxito!'
    >>> hotel.check_in('single', 2, 'invitado 1')
    False
    >>> hotel.check_in('single', 1, 'invitado 1')
    >>> hotel.booked_rooms
    {'single': {}}
    """
    # Verificar si el room_type existe en booked_rooms
    if room_type not in self.booked_rooms:
        return False
    
    # Verificar si el nombre existe en las reservas de ese tipo de habitación
    if name not in self.booked_rooms[room_type]:
        return False
    
    # Obtener la cantidad de habitaciones reservadas por esta persona
    booked_count = self.booked_rooms[room_type][name]
    
    # Verificar si room_number es mayor que la cantidad reservada
    if room_number > booked_count:
        return False
    
    # Si room_number es igual a la cantidad reservada, eliminar el nombre
    if room_number == booked_count:
        del self.booked_rooms[room_type][name]
    else:
        # Si room_number es menor, actualizar la cantidad restante
        self.booked_rooms[room_type][name] = booked_count - room_number