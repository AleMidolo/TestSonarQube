def book_room(self, room_type, room_number, name):
    """
    Verifica si hay habitaciones del tipo especificado disponibles.
    Si las habitaciones son adecuadas, modifica available_rooms y booked_rooms y finaliza la reserva, o falla en la reserva de lo contrario.
    :param room_type: str
    :param room_number: int, el número esperado de habitaciones del tipo especificado a reservar
    :param name: str, nombre del huésped
    :return: si el número de habitaciones a reservar no excede las habitaciones restantes, devuelve str '¡Éxito!'
            si excede pero la cantidad de habitaciones disponibles no es igual a cero, devuelve int (la cantidad restante de este tipo de habitación).
            si excede y la cantidad es cero o el room_type no está en available_room, devuelve False.
    >>> hotel = Hotel('hotel paz', {'single': 5, 'double': 3})
    >>> hotel.book_room('single', 1, 'huésped 1')
    '¡Éxito!'
    >>> hotel.book_room('single', 5, 'huésped 1')
    4
    >>> hotel.book_room('single', 4, 'huésped 1')
    '¡Éxito!'
    >>> hotel.book_room('single', 1, 'huésped 1')
    False
    >>> hotel.book_room('triple', 1, 'huésped 1')
    False
    """
    # Verificar si el tipo de habitación existe en available_rooms
    if room_type not in self.available_rooms:
        return False
    
    # Obtener la cantidad disponible de este tipo de habitación
    available_count = self.available_rooms[room_type]
    
    # Si no hay habitaciones disponibles
    if available_count == 0:
        return False
    
    # Si el número solicitado excede las habitaciones disponibles
    if room_number > available_count:
        return available_count
    
    # Si hay suficientes habitaciones disponibles
    # Actualizar available_rooms
    self.available_rooms[room_type] -= room_number
    
    # Actualizar booked_rooms
    if room_type not in self.booked_rooms:
        self.booked_rooms[room_type] = {}
    
    if name not in self.booked_rooms[room_type]:
        self.booked_rooms[room_type][name] = 0
    
    self.booked_rooms[room_type][name] += room_number
    
    return '¡Éxito!'