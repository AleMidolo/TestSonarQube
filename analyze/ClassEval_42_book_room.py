def book_room(self, room_type, room_number, name):
    """
        निर्दिष्ट प्रकार के कमरों की उपलब्धता की जांच करें।
        यदि कमरे पर्याप्त हैं, तो उपलब्ध_rooms और booked_rooms को संशोधित करें और बुकिंग समाप्त करें, अन्यथा बुकिंग विफल करें।
        :param room_type: str
        :param room_number: int, बुक किए जाने वाले निर्दिष्ट प्रकार के कमरों की अपेक्षित संख्या
        :param name: str, मेहमान का नाम
        :return: यदि बुक किए जाने वाले कमरों की संख्या शेष कमरों से अधिक नहीं है, तो str 'Success!' लौटाएं।
                यदि अधिक है लेकिन उपलब्ध कमरों की मात्रा शून्य के बराबर नहीं है, तो int (इस कमरे के प्रकार की शेष मात्रा) लौटाएं।
                यदि अधिक है और मात्रा शून्य है या room_type उपलब्ध_room में नहीं है, तो False लौटाएं।
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
    if room_type not in self.available_rooms:
        return False
    available = self.available_rooms[room_type]
    if room_number <= available:
        self.available_rooms[room_type] -= room_number
        if room_type not in self.booked_rooms:
            self.booked_rooms[room_type] = {}
        if name in self.booked_rooms[room_type]:
            self.booked_rooms[room_type][name] += room_number
        else:
            self.booked_rooms[room_type][name] = room_number
        return 'Success!'
    elif available == 0:
        return False
    else:
        return available