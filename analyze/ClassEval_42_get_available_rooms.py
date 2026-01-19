def get_available_rooms(self, room_type):
    """
        विशिष्ट प्रकार के उपलब्ध कमरों की संख्या प्राप्त करें।
        :param room_type: str, वह कमरे का प्रकार जिसे जानना है
        :return: int, इस प्रकार के कमरों की शेष संख्या।
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.get_available_rooms('single')
        5
        """
    if room_type in self.available_rooms:
        return self.available_rooms[room_type]
    else:
        return 0