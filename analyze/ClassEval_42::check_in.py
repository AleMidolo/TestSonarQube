class Hotel: 
    def __init__(self, name, rooms):
        """
        Initialize the three fields in Hotel System.
        name is the hotel name.
        available_rooms stores the remaining rooms in the hotel
        booked_rooms stores the rooms that have been booked and the person's name who booked rooms.
        >>> hotel.name
        'peace hotel'
        >>> hotel.available_rooms
        available_rooms = {'single': 5, 'double': 3}
        >>> hotel.booked_rooms
        {'single': {'guest 1': 2, 'guest 2':1}, 'double': {'guest1': 1}}
        """
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}

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
        if room_type not in self.available_rooms.keys():
            return False

        if room_number <= self.available_rooms[room_type]:
            if room_type not in self.booked_rooms.keys():
                self.booked_rooms[room_type] = {}
            self.booked_rooms[room_type][name] = room_number
            self.available_rooms[room_type] -= room_number
            return "Success!"
        elif self.available_rooms[room_type] != 0:
            return self.available_rooms[room_type]
        else:
            return False

    def check_out(self, room_type, room_number):
        """
        Check out rooms, add number for specific type in available_rooms.
        If room_type is new, add new type in available_rooms.
        :param room_type: str, check out room type
        :param room_number: int, check out room number
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

    def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        :param room_type: str, the room type that want to know
        :return: int, the remaining number of this type rooms.
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.get_available_rooms('single')
        5
        """
        return self.available_rooms[room_type]

    def check_in(self, room_type, room_number, name):
        """
        检查指定类型和号码的房间是否被名为 name 的人预订。
        当成功入住时（room_number 等于特定人的 booked_rooms），移除此名称。当实际入住数量（room_number）少于预订数量时，booked_rooms 中的数量将是预订数量减去实际数量。
        :param room_type: str, 入住房间类型
        :param room_number: int, 入住房间号码
        :param name: str, 人名
        :return False: 仅当 room_type 不在 booked_rooms 中或 room_number 高于 booked_rooms 中的数量时。
        >>> hotel = Hotel('和平酒店', {'single': 5, 'double': 3})
        >>> hotel.book_room('single', 1, '客人 1')
        '成功！'
        >>> hotel.check_in('single', 2, '客人 1')
        False
        >>> hotel.check_in('single', 1, '客人 1')
        >>> hotel.booked_rooms
        {'single': {}}
        """
        if room_type not in self.booked_rooms or name not in self.booked_rooms[room_type] or room_number > self.booked_rooms[room_type][name]:
            return False
        
        if room_number == self.booked_rooms[room_type][name]:
            del self.booked_rooms[room_type][name]
        else:
            self.booked_rooms[room_type][name] -= room_number