def get_available_rooms(self, room_type):
    """
        获取特定类型可用房间的数量。
        :param room_type: str, 想要了解的房间类型
        :return: int, 该类型房间的剩余数量。
        >>> hotel = Hotel('和平酒店', {'单人间': 5, '双人间': 3})
        >>> hotel.get_available_rooms('单人间')
        5
        """
    return self.available_rooms.get(room_type, 0)