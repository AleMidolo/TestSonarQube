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
    if room_type not in self.booked_rooms:
        return False
    if name not in self.booked_rooms[room_type]:
        return False
    booked_number = self.booked_rooms[room_type][name]
    if room_number > booked_number:
        return False
    if room_number == booked_number:
        del self.booked_rooms[room_type][name]
        if not self.booked_rooms[room_type]:
            del self.booked_rooms[room_type]
    else:
        self.booked_rooms[room_type][name] = booked_number - room_number