def check_out(self, room_type, room_number):
    """
    कमरों की चेक आउट करें, उपलब्ध कमरों में विशेष प्रकार के लिए संख्या जोड़ें।
    यदि room_type नया है, तो उपलब्ध_rooms में नया प्रकार जोड़ें।
    :param room_type: str, चेक आउट कमरे का प्रकार
    :param room_number: int, चेक आउट कमरे का नंबर
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