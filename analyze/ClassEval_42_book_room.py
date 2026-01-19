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
    """
    # Check if room_type exists in available_rooms
    if room_type not in self.available_rooms:
        return False
    
    # Get the current available count for this room type
    available_count = self.available_rooms[room_type]
    
    # If no rooms available, return False
    if available_count == 0:
        return False
    
    # If requested rooms exceed available rooms
    if room_number > available_count:
        return available_count
    
    # If we have enough rooms, proceed with booking
    self.available_rooms[room_type] -= room_number
    
    # Add to booked_rooms
    if name not in self.booked_rooms:
        self.booked_rooms[name] = {}
    
    if room_type not in self.booked_rooms[name]:
        self.booked_rooms[name][room_type] = 0
    
    self.booked_rooms[name][room_type] += room_number
    
    return 'Success!'