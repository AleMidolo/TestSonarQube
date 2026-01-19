def check_in(self, room_type, room_number, name):
    """
    Check if the room of the specified type and number is booked by the person named name.
    Remove this name when check in successfuly(room_number is equal to specific person's booked_rooms. When the actual check in quantity (room_number) is less than the booked quantity, number in booked_rooms will be booked quantity minus actual quantity
    :param room_type: str, check in room type
    :param room_number: int, check in room number
    :param name: str, person name
    :return False: only if the room_type is not in the booked_rooms or room_number is higher than quantity in booked rooms.
    >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
    >>> hotel.book_room('single', 1, 'guest 1')
    'Success!'
    >>> hotel.check_in('single', 2, 'guest 1')
    False
    >>> hotel.check_in('single', 1, 'guest 1')
    >>> hotel.booked_rooms
    {'single': {}}
    """
    # Check if room_type exists in booked_rooms
    if room_type not in self.booked_rooms:
        return False
    
    # Check if the person has a booking for this room type
    if name not in self.booked_rooms[room_type]:
        return False
    
    # Get the booked quantity for this person
    booked_quantity = self.booked_rooms[room_type][name]
    
    # Check if room_number is higher than booked quantity
    if room_number > booked_quantity:
        return False
    
    # Process check-in
    if room_number == booked_quantity:
        # Remove the booking entirely
        del self.booked_rooms[room_type][name]
    else:
        # Reduce the booked quantity
        self.booked_rooms[room_type][name] = booked_quantity - room_number