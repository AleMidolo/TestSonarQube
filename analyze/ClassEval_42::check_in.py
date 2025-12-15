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
        निर्दिष्ट प्रकार और संख्या का कमरा क्या उस व्यक्ति द्वारा बुक किया गया है जिसका नाम name है, यह जांचें।
        जब चेक-इन सफल हो (room_number उस विशेष व्यक्ति के booked_rooms के बराबर हो) तो इस नाम को हटा दें। जब वास्तविक चेक-इन मात्रा (room_number) बुक की गई मात्रा से कम हो, तो booked_rooms में संख्या बुक की गई मात्रा से वास्तविक मात्रा घटा दी जाएगी।
        :param room_type: str, चेक-इन कमरे का प्रकार
        :param room_number: int, चेक-इन कमरे की संख्या
        :param name: str, व्यक्ति का नाम
        :return False: केवल तभी जब room_type booked_rooms में न हो या room_number बुक किए गए कमरों की मात्रा से अधिक हो।
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.book_room('single', 1, 'guest 1')
        'Success!'
        >>> hotel.check_in('single', 2, 'guest 1')
        False
        >>> hotel.check_in('single', 1, 'guest 1')
        >>> hotel.booked_rooms
        {'single': {}}
        """
        if room_type not in self.booked_rooms or name not in self.booked_rooms[room_type] or room_number > self.booked_rooms[room_type][name]:
            return False
        
        if room_number == self.booked_rooms[room_type][name]:
            del self.booked_rooms[room_type][name]
        else:
            self.booked_rooms[room_type][name] -= room_number