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
    # Check if room_type exists in booked_rooms
    if room_type not in self.booked_rooms:
        return False
    
    # Check if the name exists in the booked_rooms for this room_type
    if name not in self.booked_rooms[room_type]:
        return False
    
    # Get the number of rooms booked by this person
    booked_count = self.booked_rooms[room_type][name]
    
    # Check if room_number exceeds the booked count
    if room_number > booked_count:
        return False
    
    # If room_number equals booked_count, remove the name
    if room_number == booked_count:
        del self.booked_rooms[room_type][name]
    else:
        # If room_number is less than booked_count, reduce the count
        self.booked_rooms[room_type][name] = booked_count - room_number