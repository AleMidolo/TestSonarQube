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
        if room_type not in self.booked_rooms.keys():
            return False
        if name in self.booked_rooms[room_type]:
            if room_number > self.booked_rooms[room_type][name]:
                return False
            elif room_number == self.booked_rooms[room_type][name]:
                self.booked_rooms[room_type].pop(name)
            else:
                self.booked_rooms[room_type][name] -= room_number

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
    
    def book_room(self, room_type, room_number, name):
        """
        检查是否有任何指定类型的房间可用。
        如果房间数量足够，修改 available_rooms 和 booked_rooms 并完成预订，否则预订失败。
        :param room_type: str
        :param room_number: int，预期预订的指定类型房间的数量
        :param name: str，客人姓名
        :return: 如果即将预订的房间数量不超过剩余房间，返回 str 'Success!'
                如果超过但可用房间数量不为零，返回 int（该房间类型的剩余数量）。
                如果超过且数量为零或 room_type 不在 available_room 中，返回 False。
        >>> hotel = Hotel('和平酒店', {'single': 5, 'double': 3})
        >>> hotel.book_room('single', 1, '客人 1')
        'Success!'
        >>> hotel.book_room('single', 5, '客人 1')
        4
        >>> hotel.book_room('single', 4, '客人 1')
        'Success!'
        >>> hotel.book_room('single', 1, '客人 1')
        False
        >>> hotel.book_room('triple', 1, '客人 1')
        False
        """
        if room_type not in self.available_rooms or self.available_rooms[room_type] < room_number:
            return False
        if self.available_rooms[room_type] >= room_number:
            if room_type not in self.booked_rooms:
                self.booked_rooms[room_type] = {}
            if name in self.booked_rooms[room_type]:
                self.booked_rooms[room_type][name] += room_number
            else:
                self.booked_rooms[room_type][name] = room_number
            self.available_rooms[room_type] -= room_number
            return 'Success!'
        remaining = self.available_rooms[room_type]
        return remaining if remaining > 0 else False