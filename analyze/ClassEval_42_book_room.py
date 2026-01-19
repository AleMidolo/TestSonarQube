def book_room(self, room_type, room_number, name):
    """
    Check if there are any rooms of the specified type available.
    if rooms are adequate, modify available_rooms and booked_rooms and finish booking, or fail to book otherwise.
    :param room_type: str
    :param room_number: int, the expected number of specified type rooms to be booked
    :param name: str, guest name
    :return: if number of rooms about to be booked doesn't exceed the remaining rooms, return str 'Success!'
            if exceeds but quantity of available rooms is not equal to zero, return int(the remaining quantity of this room type).
            if exceeds and quantity is zero or the room_type isn't in available_room, return False.
    >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
    >>> hotel.book_room('single', 1, 'guest 1')
    'Success!'
    >>> hotel.book_room('single', 5, 'guest 1')
    4
    >>> hotel.book_room('single', 4, 'guest 1')
    'Success!'
    >>> hotel.book_room('single', 1, 'guest 1')
    False
    >>> hotel.book_room('triple', 1, 'guest 1')
    False
    """
    # Check if room_type exists in available_rooms
    if room_type not in self.available_rooms:
        return False
    
    # Get the current available quantity
    available_quantity = self.available_rooms[room_type]
    
    # If no rooms available, return False
    if available_quantity == 0:
        return False
    
    # If requested rooms exceed available rooms
    if room_number > available_quantity:
        return available_quantity
    
    # If we can book the rooms, proceed with booking
    self.available_rooms[room_type] -= room_number
    
    # Add to booked_rooms
    if room_type not in self.booked_rooms:
        self.booked_rooms[room_type] = {}
    
    if name not in self.booked_rooms[room_type]:
        self.booked_rooms[room_type][name] = 0
    
    self.booked_rooms[room_type][name] += room_number
    
    return 'Success!'