def check_out(self, room_type, room_number):
    """
    退房，增加特定类型在 available_rooms 中的数量。
    如果 room_type 是新的，则在 available_rooms 中添加新类型。
    :param room_type: str, 退房房间类型
    :param room_number: int, 退房房间号
    >>> hotel = Hotel('和平酒店', {'single': 5, 'double': 3})
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